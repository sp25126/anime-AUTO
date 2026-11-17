import os
import sys
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

TOKEN_FILE = "config/youtube_token.json"
VIDEO_FILE = "output/luffy_gear5_booming_tiktok_mastered.mp4"

TITLE = "Luffy Gear 5 Drums of Liberation Viral Edit! ⚡🥁 #shorts #onepiece #luffy #gear5 #animeedit"

DESCRIPTION = """The most insane 4K Luffy Gear 5 transformation edit taking over TikTok and YouTube! The Drums of Liberation beat drop is unmatched 🔥👑

--------------------------------------------------
ORIGINAL EDIT CREDIT:
Edit by: @ZorosPasta
Track: Toma Toma
Please support the original creator for their incredible editing work!

--------------------------------------------------
DISCLAIMER (Fair Use Notice):
Copyright Disclaimer under section 107 of the Copyright Act 1976, allowance is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship, education, and research. Fair use is a use permitted by copyright statute that might otherwise be infringing. All rights belong to Toei Animation, Eiichiro Oda, Shueisha, and their respective anime production committees. No copyright infringement intended.

--------------------------------------------------
FOLLOW FOR DAILY ANIME EDITS:
YouTube: @animefandom0_0

#luffy #luffygear5 #gear5 #onepiece #onepieceedit #drumsofliberation #joyboy #anime #animeedit #animetiktok #amv #4kedit #shorts #fyp
"""

TAGS = [
    "shorts", "one piece", "luffy", "gear 5", "luffy gear 5",
    "one piece edit", "drums of liberation", "joyboy", "anime",
    "anime edit", "amv", "tiktok edit", "fyp"
]

print("[YouTube Uploader] Connecting to YouTube Data API...")
creds = Credentials.from_authorized_user_file(TOKEN_FILE)
youtube = build("youtube", "v3", credentials=creds)

body = {
    "snippet": {
        "title": TITLE,
        "description": DESCRIPTION,
        "tags": TAGS,
        "categoryId": "24" # Entertainment
    },
    "status": {
        "privacyStatus": "public", # Direct public upload to @animefandom0_0
        "selfDeclaredMadeForKids": False
    }
}

media = MediaFileUpload(
    VIDEO_FILE,
    chunksize=1024 * 1024 * 4,
    resumable=True,
    mimetype="video/mp4"
)

print(f"[YouTube Uploader] Uploading '{TITLE}'...")
request = youtube.videos().insert(
    part="snippet,status",
    body=body,
    media_body=media
)

response = None
while response is None:
    status, response = request.next_chunk()
    if status:
        print(f"  [Upload Progress] {int(status.progress() * 100)}%...", flush=True)

video_id = response.get("id")
print("\n" + "="*50)
print(f"UPLOAD SUCCESSFUL!")
print(f"Video ID: {video_id}")
print(f"Short URL: https://www.youtube.com/shorts/{video_id}")
print("="*50)
