import urllib.request
import urllib.parse
import json
import re

# High volume YouTube shorts query benchmark
queries = [
    ("moment_accidental_rizz", "bro rizzed them without knowing anime"),
    ("moment_hidden_power_flex", "bro forgot he was supposed to hide his power anime"),
    ("moment_brutal_reality_check", "the exact moment he knew he messed up anime"),
    ("moment_underdog_silences_crowd", "mc shocks everyone with his power anime short")
]

results = []

for cat_id, q in queries:
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", errors="ignore")
        # Extract titles and views
        items = re.findall(r'\"title\":\{\"runs\":\[\{\"text\":\"(.*?)\"\}\].*?\"viewCountText\":\{\"simpleText\":\"(.*?)\"\}', html)
        results.append({
            "category": cat_id,
            "query": q,
            "top_hits": items[:4]
        })
    except Exception as e:
        pass

for r in results:
    print(f"=== {r['category']} ===")
    for title, views in r['top_hits']:
        print(f"  • {title[:48]} | {views}")
