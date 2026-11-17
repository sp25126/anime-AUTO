import json
import urllib.request
import urllib.parse

with open("config/youtube_token.json") as f:
    token_data = json.load(f)

access_token = token_data.get("token")

def search_yt_api(q):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&videoDuration=short&q={urllib.parse.quote(q)}&maxResults=10"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            return data.get("items", [])
    except Exception as e:
        print("API Error:", e)
        return []

def get_channel_stats(channel_ids):
    if not channel_ids:
        return {}
    cids = ",".join(channel_ids)
    url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={cids}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            res = {}
            for ch in data.get("items", []):
                res[ch["id"]] = {
                    "title": ch["snippet"]["title"],
                    "customUrl": ch["snippet"].get("customUrl", ""),
                    "subs": int(ch["statistics"].get("subscriberCount", 0)),
                    "views": int(ch["statistics"].get("viewCount", 0)),
                    "videos": int(ch["statistics"].get("videoCount", 0)),
                }
            return res
    except Exception as e:
        print("Channels API Error:", e)
        return {}

queries = [
    "UnlimitedSky anime shorts",
    "anime couple moments shorts",
    "anime accidental rizz shorts",
    "anime funny moments shorts"
]

all_channels = {}
for q in queries:
    items = search_yt_api(q)
    for it in items:
        cid = it["snippet"]["channelId"]
        all_channels[cid] = it["snippet"]["channelTitle"]

print(f"Discovered {len(all_channels)} candidate channels. Fetching subscriber stats...")
stats = get_channel_stats(list(all_channels.keys()))

top_channels = sorted(stats.values(), key=lambda x: x["subs"], reverse=True)
print("\n=== Verified High-Sub Channels in this Category ===")
for ch in top_channels:
    subs_formatted = f"{ch['subs']/1_000_000:.2f}M" if ch['subs'] >= 1_000_000 else f"{ch['subs']//1000}K"
    print(f"• {ch['title']} ({ch['customUrl']}) | Subs: {subs_formatted} | Videos: {ch['videos']} | Total Views: {ch['views']:,}")
