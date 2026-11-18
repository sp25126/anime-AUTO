import os
import sys
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

TOKEN_FILE = "config/youtube_token.json"
VIDEO_FILE = "output/dandadan_unlimited_master.mp4"

TITLE = "Bro Really Went To A Maid Cafe Just For Him 😭 | Dandadan #shorts #dandadan #anime"

DESCRIPTION = """When you drag yourself to a maid cafe just to talk to your boy... Dandadan comedy is peak! 💀✨

--------------------------------------------------
FEATURED ANIME:
Anime: Dandadan (ダンダダン)
Characters: Ken Takakura (Okarun), Jin Enjoji (Jiji), Momo Ayase
Studio: Science SARU

--------------------------------------------------
DISCLAIMER (Fair Use Notice):
Copyright Disclaimer under section 107 of the Copyright Act 1976, allowance is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship, education, and research. Fair use is a use permitted by copyright statute that might otherwise be infringing. All rights belong to Science SARU, Yukinobu Tatsu, Shueisha, and the Dandadan Production Committee. No copyright infringement intended.

--------------------------------------------------
FOLLOW FOR DAILY ANIME MICRO-MOMENTS & EDITS:
YouTube: @animefandom0_0

#dandadan #okarun #momoayase #jiji #anime #animecomedy #animemoments #accidentalrizz #shorts #fyp #sciencesaru
"""

TAGS = [
    "shorts", "dandadan", "okarun", "momo ayase", "jiji",
    "anime funny moments", "accidental rizz", "anime comedy",
    "dandadan episode", "anime", "anime edit", "fyp", "sciencesaru"
]

# Scheduled for Thursday, Nov 19, 2026 at 7:30 PM IST (14:00:00Z)
PUBLISH_AT_ISO = "2026-11-19T14:00:00Z"

def schedule_upload():
    if not os.path.exists(VIDEO_FILE):
        print(f"Error: Video file {VIDEO_FILE} does not exist!")
        return False
        
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
        chunksize=1024 * 1024 * 2,
        resumable=True,
        mimetype="video/mp4"
    )

    print(f"[YouTube Scheduler] Uploading scheduled Short: '{TITLE}'...")
    print(f"  • Video File: {VIDEO_FILE}")
    print(f"  • Scheduled Release: Thursday, Nov 19, 2026 @ 7:30 PM IST (14:00 UTC)")

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
    print("SCHEDULED YOUTUBE UPLOAD SUCCESSFUL!")
    print(f"Video ID: {video_id}")
    print(f"Target Channel: @animefandom0_0")
    print(f"Live Status: Private (Scheduled for {PUBLISH_AT_ISO})")
    print(f"YouTube Studio Edit: https://studio.youtube.com/video/{video_id}/edit")
    print(f"Watch URL: https://youtube.com/shorts/{video_id}")
    print("="*50)
    return video_id

if __name__ == "__main__":
    schedule_upload()
