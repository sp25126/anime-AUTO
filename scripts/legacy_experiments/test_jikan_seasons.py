import requests

url = "https://api.jikan.moe/v4/seasons/now?filter=tv&limit=12"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers, timeout=10)
if res.status_code == 200:
    data = res.json().get("data", [])
    print(f"Top {len(data)} Airing Anime:")
    for a in data:
        genres = [g["name"] for g in a.get("genres", [])]
        print(f"• {a.get('title')} (MAL: {a.get('mal_id')}) | Score: {a.get('score')} | Genres: {', '.join(genres)}")
else:
    print(f"Failed: {res.status_code}")
