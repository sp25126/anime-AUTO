import urllib.request
import json
import datetime

query = """
query {
  Page(page: 1, perPage: 25) {
    media(sort: POPULARITY_DESC, type: ANIME, status: RELEASING) {
      id
      title {
        english
        romaji
      }
      popularity
      trending
      genres
      nextAiringEpisode {
        episode
        airingAt
      }
    }
  }
}
"""

req = urllib.request.Request(
    'https://graphql.anilist.co',
    data=json.dumps({'query': query}).encode('utf-8'),
    headers={'Content-Type': 'application/json', 'User-Agent': 'AnimeRadar/2.0'}
)

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for m in data['data']['Page']['media']:
            title = m['title']['english'] or m['title']['romaji']
            nxt = m.get('nextAiringEpisode')
            if nxt:
                dt = datetime.datetime.fromtimestamp(nxt['airingAt'], datetime.timezone.utc)
                day_str = dt.strftime('%a, %b %d')
                print(f"{title} | Next: Ep {nxt['episode']} on {day_str} | Pop: {m['popularity']} | Trending: {m['trending']}")
            else:
                print(f"{title} | Releasing | Pop: {m['popularity']} | Trending: {m['trending']}")
except Exception as e:
    print("Error:", e)
