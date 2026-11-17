import urllib.request
import json
import os

with open("config/youtube_token.json") as f:
    token_data = json.load(f)

# Refresh access token using refresh_token, client_id, and client_secret
refresh_token = token_data.get("refresh_token")
client_id = token_data.get("client_id")
client_secret = token_data.get("client_secret")

data = f"client_id={client_id}&client_secret={client_secret}&refresh_token={refresh_token}&grant_type=refresh_token".encode("utf-8")
req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})

try:
    with urllib.request.urlopen(req) as resp:
        tokens = json.loads(resp.read().decode())
        new_token = tokens["access_token"]
        token_data["token"] = new_token
        with open("config/youtube_token.json", "w") as f_out:
            json.dump(token_data, f_out, indent=2)
        print("Successfully refreshed YouTube API access token!")
except Exception as e:
    print("Token refresh error:", e)
