import urllib.request
import urllib.parse
import json
import re

candidates = [
    ("moment_underdog_silences_crowd", "anime underdog shocks crowd short"),
    ("moment_accidental_rizz", "bro rizz them without knowing anime short"),
    ("moment_hidden_power_flex", "bro forgot he was supposed to hide his power short"),
    ("moment_clutch_savior_arrival", "anime savior arrival chills short"),
    ("moment_touch_them_and_die", "anime mess with his girl short"),
    ("moment_brutal_reality_check", "anime cocky character reality check short")
]

results = []

for cat_id, q in candidates:
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", errors="ignore")
        matches = re.findall(r'\"title\":\{\"runs\":\[\{\"text\":\"(.*?)\"\}\].*?\"viewCountText\":\{\"simpleText\":\"(.*?)\"\}', html)
        video_ids = re.findall(r'/shorts/([a-zA-Z0-9_-]{11})', html)
        views_list = []
        for t, v in matches[:3]:
            views_list.append({"title": t, "views": v})
        results.append({
            "cat_id": cat_id,
            "query": q,
            "shorts_found": len(set(video_ids)),
            "top_samples": views_list
        })
    except Exception as e:
        pass

with open("output/best_category_research.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

for r in results:
    print(f"=== {r['cat_id']} (Shorts: {r['shorts_found']}) ===")
    for s in r['top_samples']:
        print(f"  • {s['title'][:45]} | {s['views']}")
