import json
import os
import sys
import datetime
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

TOKEN_FILE = "config/youtube_token.json"

def check_scheduled_shorts():
    if not os.path.exists(TOKEN_FILE):
        print("Error: No youtube_token.json found.")
        return
        
    creds = Credentials.from_authorized_user_file(TOKEN_FILE)
    youtube = build("youtube", "v3", credentials=creds)

    # 1. Fetch channel info
    ch_req = youtube.channels().list(part="snippet,contentDetails", mine=True)
    ch_res = ch_req.execute()
    if not ch_res.get("items"):
        print("Channel not found.")
        return
    
    ch_item = ch_res["items"][0]
    uploads_playlist_id = ch_item["contentDetails"]["relatedPlaylists"]["uploads"]
    print(f"============================================================")
    print(f"📺 Channel: {ch_item['snippet']['title']} (@animefandom0_0)")
    print(f"============================================================\n")

    # 2. Fetch the most recent uploads (both public and scheduled/private)
    print("Checking Scheduled & Recently Uploaded Videos...\n")
    p_req = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=uploads_playlist_id,
        maxResults=6
    )
    p_res = p_req.execute()

    video_ids = [it["contentDetails"]["videoId"] for it in p_res.get("items", [])]
    if not video_ids:
        print("No videos found in uploads playlist.")
        return

    v_req = youtube.videos().list(
        part="snippet,status",
        id=",".join(video_ids)
    )
    v_res = v_req.execute()

    for item in v_res.get("items", []):
        vid_id = item["id"]
        title = item["snippet"]["title"]
        status = item["status"]["privacyStatus"]
        publish_at = item["status"].get("publishAt", "Immediate/Public")
        print(f"• Title: {title}")
        print(f"  ID: {vid_id}")
        print(f"  Status: {status.upper()}")
        print(f"  Publish Schedule: {publish_at}")
        print(f"  Direct Link: https://youtube.com/shorts/{vid_id}\n")

if __name__ == "__main__":
    check_scheduled_shorts()
