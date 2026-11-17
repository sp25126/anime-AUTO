import urllib.request
import json

req = urllib.request.Request(
    'https://graphql.anilist.co',
    data=json.dumps({
        'query': '''query {
          Page(page: 1, perPage: 12) {
            media(sort: TRENDING_DESC, type: ANIME, status: RELEASING) {
              id
              title { romaji english native }
              genres
              episodes
              trending
              popularity
            }
          }
        }'''
    }).encode('utf-8'),
    headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
)

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    for m in data['data']['Page']['media']:
        eng = m['title']['english'] or m['title']['romaji']
        genres = ', '.join(m.get('genres', []))
        tr = m['trending']
        pop = m['popularity']
        print(f"[{tr} Trending | {pop} Pop] {eng} | Genres: {genres}")
