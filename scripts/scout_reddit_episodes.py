import urllib.request
import json
import re

url = 'https://www.reddit.com/r/anime/search.json?q=flair:%22Episode%22&sort=hot&t=week&limit=15'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})

try:
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode('utf-8'))
        posts = data['data']['children']
        print(f"Retrieved {len(posts)} top episode discussions this week:\n")
        for idx, p in enumerate(posts, 1):
            d = p['data']
            title = d['title']
            score = d['score']
            num_comments = d['num_comments']
            permalink = d['permalink']
            print(f"{idx}. {title}")
            print(f"   Score: {score:,} upvotes | Comments: {num_comments:,} | Link: https://reddit.com{permalink}\n")
except Exception as e:
    print("Error fetching Reddit episode discussions:", e)
