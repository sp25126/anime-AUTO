import urllib.request
import urllib.parse
import re

def search_ddg(query):
    url = 'https://html.duckduckgo.com/html/?q=' + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
            links = re.findall(r'uddg=([^&]+)', html)
            decoded = [urllib.parse.unquote(l) for l in links]
            filtered = [l for l in decoded if 'tiktok.com' in l or 'instagram.com/reel' in l or 'youtube.com' in l]
            print(f"Query: '{query}' -> Found {len(filtered)} results:")
            for item in filtered[:5]:
                print("  *", item)
            return filtered
    except Exception as e:
        print("Error searching DDG:", e)
        return []

if __name__ == '__main__':
    search_ddg('site:tiktok.com anime rizz moment')
    search_ddg('site:instagram.com/reel anime rizz')
