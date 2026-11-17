"""
Multi-Horizon Dynamic Trend Comparator
Ingests Daily (24h), Weekly (7d), and Monthly (30d) anime engagement signals,
ranks candidate moments using multi-factor scoring, and selects the winning moment.
"""

import json
import urllib.request
import urllib.parse
import datetime
import os
import sys

def fetch_anilist_data():
    query = """
    query {
      daily: Page(page: 1, perPage: 20) {
        media(sort: TRENDING_DESC, type: ANIME, status: RELEASING) {
          id
          title { english romaji }
          trending
          popularity
          genres
          nextAiringEpisode { episode airingAt }
        }
      }
      weekly: Page(page: 1, perPage: 25) {
        media(sort: POPULARITY_DESC, type: ANIME, seasonYear: 2026, status: RELEASING) {
          id
          title { english romaji }
          trending
          popularity
          genres
        }
      }
      monthly: Page(page: 1, perPage: 25) {
        media(sort: SCORE_DESC, type: ANIME, format: TV) {
          id
          title { english romaji }
          averageScore
          popularity
          genres
        }
      }
    }
    """
    url = "https://graphql.anilist.co"
    req = urllib.request.Request(
        url,
        data=json.dumps({"query": query}).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "AnimeRadar/3.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            return json.loads(resp.read().decode())["data"]
    except Exception as e:
        print("AniList Fetch Error:", e)
        return None

def score_anime_candidates(data, target_format="GROUP_C"):
    """
    target_format: 'GROUP_A' (Edit Ranking) or 'GROUP_C' (Micro-Moment)
    """
    daily_items = {m["id"]: m for m in data.get("daily", {}).get("media", [])}
    weekly_items = {m["id"]: m for m in data.get("weekly", {}).get("media", [])}
    monthly_items = {m["id"]: m for m in data.get("monthly", {}).get("media", [])}
    
    all_ids = set(daily_items.keys()) | set(weekly_items.keys()) | set(monthly_items.keys())
    
    scored = []
    for mid in all_ids:
        title_obj = (daily_items.get(mid) or weekly_items.get(mid) or monthly_items.get(mid))["title"]
        title = title_obj.get("english") or title_obj.get("romaji")
        genres = (daily_items.get(mid) or weekly_items.get(mid) or monthly_items.get(mid)).get("genres", [])
        
        # 1. Daily Velocity (0-100)
        daily_score = 0
        if mid in daily_items:
            daily_score = min(daily_items[mid]["trending"] / 3.5, 100)
            
        # 2. Weekly Popularity (0-100)
        weekly_score = 0
        if mid in weekly_items:
            weekly_score = min(weekly_items[mid]["popularity"] / 1500, 100)
            
        # 3. Monthly Evergreen Score (0-100)
        monthly_score = 0
        if mid in monthly_items:
            monthly_score = monthly_items[mid].get("averageScore", 70)
            
        # Format-specific weighting
        if target_format == "GROUP_C": # Micro-Moment / Accidental Rizz
            # Bonus for Romance, Comedy, Slice of Life
            genre_bonus = 20 if any(g in ["Romance", "Comedy", "Slice of Life"] for g in genres) else 0
            final_score = (0.50 * daily_score) + (0.35 * weekly_score) + (0.15 * monthly_score) + genre_bonus
            archetype = "Micro-Moment / Rizz / Deadpan Banter"
            bg_recommendation = "romcom_sunset.webp" if "Romance" in genres else "ghibli_meadow.jpg"
        else: # GROUP_A: Edit Ranking / Sakuga Climax
            # Bonus for Action, Fantasy, Sci-Fi
            genre_bonus = 20 if any(g in ["Action", "Fantasy", "Sci-Fi"] for g in genres) else 0
            final_score = (0.45 * daily_score) + (0.40 * weekly_score) + (0.15 * monthly_score) + genre_bonus
            archetype = "Sakuga Climax / Cold Aura Flex"
            bg_recommendation = "sakuga_lightning.jpg" if "Action" in genres else "cyberpunk_moon.jpg"
            
        scored.append({
            "id": mid,
            "title": title,
            "genres": genres,
            "daily_trend": daily_score,
            "weekly_pop": weekly_score,
            "monthly_score": monthly_score,
            "final_score": round(final_score, 1),
            "archetype": archetype,
            "bg_recommendation": bg_recommendation
        })
        
    scored.sort(key=lambda x: x["final_score"], reverse=True)
    return scored

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "GROUP_C"
    print(f"=== Running Multi-Horizon Trend Comparator for {mode} ===")
    data = fetch_anilist_data()
    if data:
        results = score_anime_candidates(data, target_format=mode)
        print(f"\nTop 5 Ranked Candidates for {mode}:")
        for i, cand in enumerate(results[:5], 1):
            print(f"{i}. {cand['title']} (Score: {cand['final_score']})")
            print(f"   Genres: {', '.join(cand['genres'][:3])} | Recommended BG: {cand['bg_recommendation']}")
            print(f"   Archetype: {cand['archetype']}\n")
        
        # Save snapshot
        os.makedirs("analysis", exist_ok=True)
        with open(f"analysis/multi_horizon_{mode.lower()}.json", "w") as f:
            json.dump(results, f, indent=2)
        print(f"Saved ranking matrix to analysis/multi_horizon_{mode.lower()}.json")
