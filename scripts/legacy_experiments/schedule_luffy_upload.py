import os
import sys
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

TOKEN_FILE = "config/youtube_token.json"
VIDEO_FILE = "output/luffy_gear5_vertical_mastered.mp4"

TITLE = "Luffy Gear 5 Drums of Liberation Insane Edit! ⚡🥁 #shorts #onepiece #luffy #gear5"

DESCRIPTION = """The most insane 4K Luffy Gear 5 transformation edit taking over TikTok! The Drums of Liberation beat drop is unmatched 🔥👑

--------------------------------------------------
ORIGINAL EDIT CREDIT:
Edit by: @Molob
Track: Brazilian Phonk / Drums of Liberation
Support the original creator and subscribe to their channel for more insane 4K edits!

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

# Scheduled for Friday, Nov 20, 2026 at 7:30 PM IST (14:00 UTC)
# Avoids all conflict with Sunday, Monday, Tuesday, Wednesday uploads!
PUBLISH_AT_ISO = "2026-11-20T14:00:00Z"

print(f"[YouTube Scheduler] Connecting to YouTube API...")
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
        "privacyStatus": "private", # Must be private for scheduled publish
        "publishAt": PUBLISH_AT_ISO,
        "selfDeclaredMadeForKids": False
    }
}

media = MediaFileUpload(
    VIDEO_FILE,
    chunksize=1024 * 1024 * 4,
    resumable=True,
    mimetype="video/mp4"
)

print(f"[YouTube Scheduler] Uploading scheduled Short: '{TITLE}'...")
print(f"  • Scheduled Release: Friday, Nov 20 @ 7:30 PM IST (14:00 UTC)")

request = youtube.videos().insert(
    part="snippet,status",
    body=body,
    media_body=media
)

response = None
while response is None:
    status, response = request.next_chunk()
    if status:
        print(f"  [Progress] {int(status.progress() * 100)}%...", flush=True)

video_id = response.get("id")
print("\n" + "="*50)
print(f"SCHEDULED UPLOAD SUCCESSFUL!")
print(f"Video ID: {video_id}")
print(f"Live Status: Private (Scheduled for {PUBLISH_AT_ISO})")
print(f"Preview URL: https://studio.youtube.com/video/{video_id}/edit")
print("="*50)
