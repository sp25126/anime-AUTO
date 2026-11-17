import urllib.request
import urllib.parse
import json
import re

queries = [
    ("Luffy Gear 5", "luffy gear 5 transformation short"),
    ("Ash Greninja", "ash greninja evolution short"),
    ("Asuna & Kirito", "asuna saves kirito short"),
    ("Gojo Hollow Purple", "gojo hollow purple short"),
    ("Sukuna Malevolent Shrine", "sukuna malevolent shrine shibuya short"),
    ("Eren Founding Titan", "eren declares war short")
]

results = []

for category, q in queries:
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", errors="ignore")
        matches = re.findall(r'\"title\":\{\"runs\":\[\{\"text\":\"(.*?)\"\}\].*?\"viewCountText\":\{\"simpleText\":\"(.*?)\"\}', html)
        for t, v in matches[:2]:
            results.append({"category": category, "title": t, "views": v})
    except Exception as e:
        pass

for r in results:
    print(f"[{r['category']}] {r['title'][:40]} | {r['views']}")

with open("output/single_moments_research.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
