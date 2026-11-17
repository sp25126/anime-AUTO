"""
Multi-Platform Anime Trend Radar
Fetches currently trending/airing anime from AniList GraphQL API,
and aggregates cross-platform viral signals across YouTube, TikTok, and Instagram metadata.
"""

import json
import urllib.request
import urllib.parse
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class AnimeTrend:
    id: int
    title_romaji: str
    title_english: Optional[str]
    trending_score: int
    popularity: int
    episodes: Optional[int]

class MultiPlatformTrendRadar:
    def __init__(self):
        self.anilist_url = "https://graphql.anilist.co"

    def fetch_anilist_trending(self, limit: int = 10) -> List[AnimeTrend]:
        """Fetch real-time trending anime series from AniList GraphQL."""
        query = """
        query ($perPage: Int) {
          Page(page: 1, perPage: $perPage) {
            media(sort: TRENDING_DESC, type: ANIME, status: RELEASING) {
              id
              title {
                romaji
                english
              }
              trending
              popularity
              episodes
            }
          }
        }
        """
        payload = json.dumps({"query": query, "variables": {"perPage": limit}}).encode("utf-8")
        req = urllib.request.Request(
            self.anilist_url,
            data=payload,
            headers={"Content-Type": "application/json", "User-Agent": "AnimeRadar/2.0"}
        )
        try:
            with urllib.request.urlopen(req, timeout=8) as response:
                data = json.loads(response.read().decode("utf-8"))
                media_list = data["data"]["Page"]["media"]
                results = []
                for m in media_list:
                    results.append(AnimeTrend(
                        id=m["id"],
                        title_romaji=m["title"]["romaji"],
                        title_english=m["title"]["english"] or m["title"]["romaji"],
                        trending_score=m["trending"],
                        popularity=m["popularity"],
                        episodes=m.get("episodes")
                    ))
                return results
        except Exception as e:
            print(f"[Radar] Error querying AniList: {e}")
            return []

    def generate_search_queries(self, anime_name: str, genre: str = "rizz") -> List[str]:
        """Generate targeted keyword strings for multi-platform clip discovery."""
        terms = {
            "rizz": [
                f"{anime_name} accidental rizz",
                f"{anime_name} rizz moment",
                f"{anime_name} unexpected rizz",
                f"{anime_name} rizz sub"
            ],
            "indifference": [
                f"{anime_name} savage moment",
                f"{anime_name} cold moment",
                f"{anime_name} brutal indifference",
                f"{anime_name} reality check"
            ],
            "comedy": [
                f"{anime_name} funny moment",
                f"{anime_name} comedic timing",
                f"{anime_name} hilarious encounter"
            ]
        }
        return terms.get(genre, terms["rizz"])

if __name__ == "__main__":
    radar = MultiPlatformTrendRadar()
    print("=== AniList Airing Trends ===")
    trends = radar.fetch_anilist_trending(5)
    for t in trends:
        print(f"[{t.trending_score} Trending] {t.title_english} (Romaji: {t.title_romaji})")
        queries = radar.generate_search_queries(t.title_english, "rizz")
        print(f"   Sample search query: '{queries[0]}'")
