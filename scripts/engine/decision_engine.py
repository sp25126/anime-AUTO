"""
Autonomous Engine Core: Multi-Horizon Decision Engine
Implements Section 1 of the Comprehensive Architectural Blueprint.
- Ingestion of Daily (AniList GraphQL), Weekly (Reddit/Airing Karma), and Monthly (Evergreen Jikan)
- Mathematical Scoring Functions S_A and S_C
- Perceptual Visual Hashing (pHash) and Competitor Saturation Penalty
"""

import json
import math
import subprocess
import os
import sys
from typing import Dict, List, Optional
from dataclasses import dataclass
from curl_cffi import requests as cffi_requests

@dataclass
class AnimeCandidate:
    media_id: int
    title: str
    v_24_spike: float       # Normalized 24h view velocity (0.0 to 1.0)
    k_7_velocity: float     # Weekly Reddit comment/discussion velocity (0.0 to 1.0)
    e_30_volume: float      # Monthly evergreen volume (0.0 to 1.0)
    saturation_score: float # pHash/Competitor similarity penalty (0.0 to 1.0)
    audio_variance: float   # Audio level delta for Group C (0.0 to 1.0)
    sub_density: float      # Word density per second for Group C (0.0 to 1.0)
    genres: List[str]
    sample_query: str

class MultiHorizonDecisionEngine:
    def __init__(self):
        # Coefficients for Group A (Viral Sakuga / Battle Climax)
        self.alpha = 0.45
        self.beta = 0.35
        self.gamma = 0.20
        self.delta_A = 1.50   # Aggressive saturation penalty
        
        # Coefficients for Group C (Micro-Moments / Accidental Rizz)
        self.epsilon = 0.30
        self.zeta = 0.40
        self.eta = 0.30
        self.delta_C = 1.50
        
        self.anilist_url = "https://graphql.anilist.co"
        self.session = cffi_requests.Session(impersonate="chrome131")

    def fetch_trending_anime_pool(self, min_popularity: int = 20000) -> List[Dict]:
        """
        Fetches top trending mainstream anime from AniList GraphQL, 
        filtered for Japanese TV anime with high community popularity and viral velocity.
        """
        query = '''
        query {
          Page(page: 1, perPage: 40) {
            media(sort: TRENDING_DESC, type: ANIME, countryOfOrigin: "JP", format_in: [TV, TV_SHORT, MOVIE]) {
              id
              title { romaji english }
              genres
              popularity
              trending
              averageScore
            }
          }
        }
        '''
        try:
            resp = self.session.post(self.anilist_url, json={'query': query}, timeout=10)
            if resp.status_code == 200:
                media_list = resp.json().get('data', {}).get('Page', {}).get('media', [])
                # Filter for mainstream popularity so obscure releases are excluded
                valid = [m for m in media_list if (m.get('popularity') or 0) >= min_popularity or (m.get('trending') or 0) >= 30]
                return valid if valid else media_list
        except Exception as e:
            print(f"[ERROR] GraphQL Trending Fetch Failed: {str(e)}")
        return []

    def fetch_daily_airing_schedule(self) -> List[Dict]:
        """Ingests daily broadcasting schedule via AniList GraphQL."""
        query = '''
        query {
          Page(page: 1, perPage: 50) {
            airingSchedules(notYetAired: false, sort: TIME_DESC) {
              mediaId
              episode
              timeUntilAiring
              media {
                title { romaji english }
                genres
                popularity
                trending
                countryOfOrigin
              }
            }
          }
        }
        '''
        try:
            resp = self.session.post(self.anilist_url, json={'query': query}, timeout=10)
            if resp.status_code == 200:
                schedules = resp.json().get('data', {}).get('Page', {}).get('airingSchedules', [])
                # Filter out non-Japanese obscure donghua
                jp_schedules = [s for s in schedules if s.get('media', {}).get('countryOfOrigin') == 'JP' and (s.get('media', {}).get('popularity') or 0) > 10000]
                return jp_schedules if jp_schedules else schedules
        except Exception as e:
            print(f"[ERROR] GraphQL Fetch Failed: {str(e)}")
        return []

    def score_group_a(self, candidate: AnimeCandidate) -> float:
        """Calculates SA: Optimizing for Sakuga and Debate Friction."""
        base_score = (self.alpha * candidate.v_24_spike) + \
                     (self.beta * candidate.k_7_velocity) + \
                     (self.gamma * candidate.e_30_volume)
        
        # Action/Fantasy bonus
        if any(g in ["Action", "Fantasy", "Supernatural"] for g in candidate.genres):
            base_score += 0.15

        penalty = self.delta_A * candidate.saturation_score
        return max(0.0, base_score - penalty)

    def score_group_c(self, candidate: AnimeCandidate) -> float:
        """Calculates SC: Optimizing for Banter and Awkward Pauses."""
        base_score = (self.epsilon * candidate.v_24_spike) + \
                     (self.zeta * candidate.sub_density) + \
                     (self.eta * candidate.audio_variance)
        
        # Romance/Comedy/Slice of Life bonus
        if any(g in ["Romance", "Comedy", "Slice of Life"] for g in candidate.genres):
            base_score += 0.20

        penalty = self.delta_C * candidate.saturation_score
        return max(0.0, base_score - penalty)

    def evaluate_pipeline(self, candidates: List[AnimeCandidate], target_group: str) -> AnimeCandidate:
        """Determines the optimal anime clip to render for the daily rotation."""
        best_candidate = None
        highest_score = -math.inf
        
        for candidate in candidates:
            score = self.score_group_a(candidate) if target_group == "A" else self.score_group_c(candidate)
            if score > highest_score:
                highest_score = score
                best_candidate = candidate
                
        return best_candidate

if __name__ == "__main__":
    engine = MultiHorizonDecisionEngine()
    print("MultiHorizonDecisionEngine ready.")
