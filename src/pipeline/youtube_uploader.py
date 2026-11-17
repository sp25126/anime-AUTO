import os
import sys
import json
import time
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube"]
CLIENT_SECRETS_FILE = "config/client_secrets.json"
TOKEN_PICKLE_FILE = "config/youtube_token.json"

def get_authenticated_service():
    os.makedirs("config", exist_ok=True)
    creds = None
    
    if os.path.exists(TOKEN_PICKLE_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_PICKLE_FILE, SCOPES)
        except Exception as e:
            print(f"[Auth] Existing token failed: {e}")
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("[Auth] Refreshing expired credentials...")
            creds.refresh(Request())
        else:
            if not os.path.exists(CLIENT_SECRETS_FILE):
                print(f"[Auth Error] '{CLIENT_SECRETS_FILE}' not found!")
                print("Please download OAuth 2.0 Client ID Credentials JSON from Google Cloud Console")
                print("and save it as: config/client_secrets.json")
                return None
            print("[Auth] Starting local browser authorization flow...")
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_PICKLE_FILE, "w", encoding="utf-8") as token_file:
            token_file.write(creds.to_json())
        print(f"[Auth] Saved authorized token to {TOKEN_PICKLE_FILE}")

    return build("youtube", "v3", credentials=creds)

def upload_short(
    file_path,
    title,
    description,
    tags=None,
    category_id="24", # Entertainment
    privacy_status="public" # "public", "private", or "unlisted"
):
    if not os.path.exists(file_path):
        print(f"[Upload Error] Video file not found: {file_path}")
        return None

    youtube = get_authenticated_service()
    if not youtube:
        return None

    # Ensure title contains #shorts for YouTube shorts shelf indexing
    if "#shorts" not in title.lower():
        title = f"{title} #shorts"

    body = {
        "snippet": {
            "title": title[:100], # Max 100 chars
            "description": description,
            "tags": tags or ["shorts", "anime", "animeedit"],
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": privacy_status,
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(
        file_path,
        chunksize=1024*1024*4, # 4MB chunks
        resumable=True,
        mimetype="video/mp4"
    )

    print(f"\n[YouTube Uploader] Uploading: {file_path}")
    print(f"  • Title: {body['snippet']['title']}")
    print(f"  • Privacy: {privacy_status}")

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"  [Progress] Uploaded {int(status.progress() * 100)}%...")

    video_id = response.get("id")
    video_url = f"https://www.youtube.com/shorts/{video_id}"
    print(f"\n[Upload Success] Video live at: {video_url}")
    return response

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Upload YouTube Shorts")
    parser.add_argument("--file", help="Path to video file")
    parser.add_argument("--title", help="Short Title")
    parser.add_argument("--desc", help="Short Description")
    parser.add_argument("--privacy", default="public", choices=["public", "unlisted", "private"])
    args = parser.parse_args()

    if args.file and args.title:
        upload_short(args.file, args.title, args.desc or "", privacy_status=args.privacy)
    else:
        print("YouTube Uploader initialized. Run with --file and --title, or check auth credentials.")
        get_authenticated_service()
