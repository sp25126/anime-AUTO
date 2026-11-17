import json
import urllib.request
import os

with open("config/youtube_token.json") as f:
    token_data = json.load(f)

# Inspect token structure
print("Token keys:", list(token_data.keys()))
