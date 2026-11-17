import json
import urllib.request

with open("config/youtube_token.json") as f:
    token_data = json.load(f)
access_token = token_data.get("token")

# Let's inspect uploads for @animequick-ha and @badass020
channel_handles = ["animequick-ha", "badass020", "anime__ntr", "unlimitedskyyy"]

for handle in channel_handles:
    # Get channel uploads playlist ID
    url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails,snippet,statistics&forHandle={handle}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            items = data.get("items", [])
            if not items:
                continue
            item = items[0]
            uploads_id = item["contentDetails"]["relatedPlaylists"]["uploads"]
            subs = item["statistics"]["subscriberCount"]
            views = item["statistics"]["viewCount"]
            videos = item["statistics"]["videoCount"]
            print(f"\n==========================================")
            print(f"Channel: {item['snippet']['title']} (@{handle})")
            print(f"Subscribers: {int(subs):,} | Total Views: {int(views):,} | Videos: {videos}")
            
            # Fetch latest 5 videos from uploads playlist
            v_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={uploads_id}&maxResults=5"
            v_req = urllib.request.Request(v_url, headers={"Authorization": f"Bearer {access_token}"})
            with urllib.request.urlopen(v_req) as v_resp:
                v_data = json.loads(v_resp.read().decode())
                for v in v_data.get("items", []):
                    snip = v["snippet"]
                    print(f"  • [{snip['publishedAt'][:10]}] {snip['title']}")
    except Exception as e:
        print(f"Error for {handle}:", e)
