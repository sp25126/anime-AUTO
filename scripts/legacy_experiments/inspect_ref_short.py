import urllib.request
import re

url = "https://www.youtube.com/shorts/4UmxVntdbsI"
req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
)

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8", errors="ignore")

    title = re.findall(r"<title>(.*?)</title>", html)
    print("TITLE:", title)

    # find description or text
    author = re.findall(r'"ownerChannelName":"([^"]+)"', html)
    print("AUTHOR:", author[:2])

    desc = re.findall(r'"shortDescription":"([^"]+)"', html)
    print("DESC:", desc[:2] if desc else "None")

    # Look for view count
    views = re.findall(r'"viewCount":"(\d+)"', html)
    print("VIEWS:", views[:2] if views else "None")

except Exception as e:
    print("ERROR:", e)
