"""
Jikan API v4 (MyAnimeList) and AniList metadata client.
Fetches canonical anime metadata, studio attribution, MAL scores, and genres with local disk caching.
"""

import os
import json
import time
import requests
from typing import Optional, Dict, Any

CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cache", "anime_meta")
os.makedirs(CACHE_DIR, exist_ok=True)

class JikanClient:
    BASE_URL = "https://api.jikan.moe/v4"
    
    @staticmethod
    def _slugify(text: str) -> str:
        return "".join(c if c.isalnum() else "_" for c in text.lower()).strip("_")
    
    @classmethod
    def search_anime(cls, title: str) -> Optional[Dict[str, Any]]:
        slug = cls._slugify(title)
        cache_file = os.path.join(CACHE_DIR, f"{slug}.json")
        
        if os.path.exists(cache_file):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
                
        url = f"{cls.BASE_URL}/anime"
        params = {"q": title, "limit": 1}
        
        try:
            # Respect rate limit
            time.sleep(0.35)
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json().get("data", [])
                if data:
                    anime = data[0]
                    studios = [s.get("name", "") for s in anime.get("studios", [])]
                    genres = [g.get("name", "") for g in anime.get("genres", [])]
                    
                    clean_meta = {
                        "mal_id": anime.get("mal_id"),
                        "title_english": anime.get("title_english") or anime.get("title"),
                        "title_japanese": anime.get("title_japanese"),
                        "score": anime.get("score"),
                        "scored_by": anime.get("scored_by"),
                        "rank": anime.get("rank"),
                        "popularity": anime.get("popularity"),
                        "year": anime.get("year"),
                        "studios": studios,
                        "primary_studio": studios[0] if studios else "Unknown Studio",
                        "genres": genres,
                        "episodes": anime.get("episodes"),
                        "synopsis": anime.get("synopsis")
                    }
                    
                    with open(cache_file, "w", encoding="utf-8") as f:
                        json.dump(clean_meta, f, indent=2)
                    return clean_meta
        except Exception as e:
            print(f"[JikanClient] Error fetching '{title}': {e}")
            
        return None

if __name__ == "__main__":
    meta = JikanClient.search_anime("Jujutsu Kaisen")
    print(json.dumps(meta, indent=2))
