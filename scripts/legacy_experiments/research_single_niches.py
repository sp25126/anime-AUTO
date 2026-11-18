import urllib.request
import urllib.parse
import json
import re

# High performing single-moment niches on YouTube Shorts
searches = [
    ("Unaware OP Protagonist", "anime bro forgot he was supposed to hide his power short"),
    ("Accidental Rizz & Flustered", "anime bro rizz them without knowing short"),
    ("Cold Disrespect / Verbal Humiliation", "coldest anime disrespect scene short"),
    ("Sacrifice & Tear-Jerking Goodbyes", "saddest anime death scene short"),
    ("Betrayal & Shock Plot Twists", "anime biggest betrayal scene short"),
    ("Sudden Rage / Snap Moment", "anime character snaps rage scene short"),
    ("Stupid / Goofy Deranged Gags", "funniest anime unhinged moments short"),
    ("Villain Teaches A Brutal Lesson", "anime villain reality check scene short")
]

analytics = []

for niche, q in searches:
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", errors="ignore")
        matches = re.findall(r'\"title\":\{\"runs\":\[\{\"text\":\"(.*?)\"\}\].*?\"viewCountText\":\{\"simpleText\":\"(.*?)\"\}', html)
        top_samples = []
        for t, v in matches[:3]:
            top_samples.append({"title": t, "views": v})
        analytics.append({
            "niche": niche,
            "query": q,
            "samples": top_samples
        })
    except Exception as e:
        pass

with open("output/single_moments_deep_research.json", "w", encoding="utf-8") as f:
    json.dump(analytics, f, indent=2)

for a in analytics:
    print(f"=== {a['niche']} ===")
    for s in a['samples']:
        print(f"  • {s['title'][:45]} | {s['views']}")
