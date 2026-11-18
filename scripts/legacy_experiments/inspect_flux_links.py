import urllib.request
import re

links = [
    ("Rank 1", "https://youtube.com/shorts/5PU7EiTPlas"),
    ("Rank 2", "https://youtube.com/shorts/4DgUbmHM29c"),
    ("Rank 3", "https://youtube.com/shorts/8ff_ILEHRIk"),
    ("Rank 4", "https://youtube.com/shorts/ZVnewMXIr0k"),
    ("Rank 5", "https://youtube.com/shorts/bR65h-U16Sk")
]

for rank, url in links:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            title = re.findall(r"<title>(.*?)</title>", html)
            views = re.findall(r'"viewCount":"([^"]+)"', html)
            print(f"{rank}: {title[0] if title else url} | Views: {views[0] if views else 'N/A'}")
    except Exception as e:
        print(f"{rank}: Error {e}")
