import urllib.request
import json
import datetime

query = """
query ($weekStart: Int, $weekEnd: Int) {
  Page(page: 1, perPage: 50) {
    airingSchedules(airingAt_greater: $weekStart, airingAt_lesser: $weekEnd, sort: TIME) {
      airingAt
      episode
      media {
        id
        title {
          romaji
          english
        }
        popularity
        trending
        genres
      }
    }
  }
}
"""

now = datetime.datetime.now(datetime.timezone.utc)
# Start of week: Monday
start_of_week = now - datetime.timedelta(days=now.weekday())
start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
end_of_week = start_of_week + datetime.timedelta(days=7)

start_ts = int(start_of_week.timestamp())
end_ts = int(end_of_week.timestamp())

url = "https://graphql.anilist.co"
payload = json.dumps({
    "query": query,
    "variables": {"weekStart": start_ts, "weekEnd": end_ts}
}).encode("utf-8")

req = urllib.request.Request(
    url,
    data=payload,
    headers={"Content-Type": "application/json", "User-Agent": "AnimeRadar/2.0"}
)

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        schedules = data["data"]["Page"]["airingSchedules"]
        
        shows = {}
        for s in schedules:
            m = s["media"]
            mid = m["id"]
            if mid not in shows:
                shows[mid] = {
                    "title": m["title"]["english"] or m["title"]["romaji"],
                    "romaji": m["title"]["romaji"],
                    "episode": s["episode"],
                    "airingAt": s["airingAt"],
                    "popularity": m["popularity"],
                    "trending": m["trending"],
                    "genres": m["genres"]
                }
        
        sorted_shows = sorted(shows.values(), key=lambda x: (x["trending"], x["popularity"]), reverse=True)
        print(f"Total Airing Shows Found This Week: {len(sorted_shows)}\n")
        
        # Group by day of week
        by_day = {}
        for s in sorted_shows:
            dt = datetime.datetime.fromtimestamp(s["airingAt"], datetime.timezone.utc)
            day_name = dt.strftime("%A (%b %d)")
            if day_name not in by_day:
                by_day[day_name] = []
            by_day[day_name].append((s, dt.strftime("%H:%M UTC")))
            
        for day, items in by_day.items():
            print(f"=== {day} ===")
            for s, air_time in items[:6]:
                genres_str = ", ".join(s["genres"][:3])
                print(f"  • {s['title']} (Ep {s['episode']}) - {air_time} [Trending: {s['trending']}] [{genres_str}]")
            print()

except Exception as e:
    print("Error:", e)
