import json
import urllib.request
import urllib.parse

with open("config/youtube_token.json") as f:
    token_data = json.load(f)
access_token = token_data.get("token")

# Let's inspect the latest 3 videos and publishing dates for the top channels
channels_to_audit = [
    ("badass020", "UCq1bKeq9cQoW0qY8v3J3LpA", "@badass020"),
    ("Anime Quick", "UCt4jY4b1w8P9X0h0m5qZ1nA", "@animequick-ha"),
    ("Anime Ntr", "UCyV5m-HhYf8u8iE6w8JvVqA", "@anime__ntr"),
    ("Potatoy113", "UCY0KzB8Vn9u1w7x6z5y4x3w", "@potatoy113"),
    ("Unlimited Sky", "UC4F4_g6L8D3v1Fk5b8S0wLA", "@unlimitedskyyy")
]

print("=== Benchmarking Daily Publishing Cadence ===")
# We will inspect their recent uploads playlist or search by channelId
for ch_name, handle in [("badass020", "@badass020"), ("Anime Quick", "@animequick-ha"), ("Potatoy113", "@potatoy113"), ("Unlimited Sky", "@unlimitedskyyy")]:
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&videoDuration=short&q={urllib.parse.quote(ch_name)}&maxResults=4"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"\nChannel: {ch_name} ({handle})")
            for it in data.get("items", []):
                snippet = it["snippet"]
                print(f"  • [{snippet['publishedAt'][:10]}] {snippet['title']}")
    except Exception as e:
        print(f"Error for {ch_name}:", e)
