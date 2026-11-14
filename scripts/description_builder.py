"""
Description and Credit Attribution Builder for Anime Compilation Engine.
Generates compliant, rich YouTube descriptions with full creator credits,
anime title/studio attribution, music credits, and legal fair-use disclaimers.
"""

from typing import List, Dict, Any

def build_youtube_description(
    subcategory_meta: Dict[str, Any],
    clips_attribution: List[Dict[str, Any]],
    music_meta: Dict[str, Any] = None
) -> str:
    sub_name = subcategory_meta.get("name", "ANIME COMPILATION")
    focus = subcategory_meta.get("focus", "Peak Anime Moments")
    tags = subcategory_meta.get("description_tags", ["#shorts", "#anime"])
    
    lines = []
    
    # Header & Hook
    lines.append(f"🏆 {sub_name} — {focus}")
    lines.append("Which anime took the #1 spot? Drop your personal ranking in the comments! 👇🔥\n")
    
    # Clip-by-Clip Attribution (Rank 5 down to Rank 1)
    lines.append("══════════════════════════════════════════")
    lines.append("🎬 FEATURED CLIPS & CREATOR CREDITS:")
    lines.append("══════════════════════════════════════════")
    
    for clip in clips_attribution:
        rank = clip.get("rank", "?")
        level = clip.get("level", f"Level {rank}")
        anime = clip.get("anime_title", "Anime Masterpiece")
        studio = clip.get("studio", "")
        studio_str = f" [Studio: {studio}]" if studio else ""
        creator = clip.get("original_creator", "")
        platform = clip.get("platform", "Web")
        source_url = clip.get("source_url", "")
        
        if creator and creator != "Unknown":
            creator_line = f" • Edit by: {creator} ({platform})"
        else:
            creator_line = " • Official Animation Footage"
            
        link_str = f" | Source: {source_url}" if source_url else ""
        
        lines.append(f"[{level}] Rank {rank}: {anime}{studio_str}{creator_line}{link_str}")

    lines.append("")
    
    # Music Credits
    lines.append("══════════════════════════════════════════")
    lines.append("🎵 MUSIC & AUDIO CREDITS:")
    lines.append("══════════════════════════════════════════")
    if music_meta:
        track_name = music_meta.get("track_name", "Anime Soundtrack")
        artist = music_meta.get("artist", "Respective Sound Artist")
        source = music_meta.get("source_url", "")
        lines.append(f"• Audio Bed: {track_name} by {artist}")
        if source:
            lines.append(f"• Music Source: {source}")
    else:
        lines.append(f"• Audio Bed: {subcategory_meta.get('audio_genre', 'Anime High-Energy Sound Bed')}")
    lines.append("")
    
    # Fair Use & Disclaimer
    lines.append("══════════════════════════════════════════")
    lines.append("⚖️ COPYRIGHT & FAIR USE DISCLAIMER:")
    lines.append("══════════════════════════════════════════")
    lines.append("All footages, audio, edits, and characters used in this video belong to their respective anime studios, animators, and content creators.")
    lines.append("This video is a transformative commentary and ranking compilation created under Fair Use guidelines (Section 107 of the Copyright Act 1976).")
    lines.append("Full credit is proudly given to the talented creators, editors, and studios credited above.\n")
    
    # Hashtags
    lines.append(" ".join(tags))
    
    return "\n".join(lines)

if __name__ == "__main__":
    test_sub = {
      "name": "TRENDING ANIME EDITS",
      "focus": "Viral Velocity, Twixtor Flow & Phonk Transitions",
      "description_tags": ["#shorts", "#anime", "#animeedit", "#sakuga"]
    }
    test_clips = [
      {
        "rank": "5",
        "level": "Level 1",
        "anime_title": "Jujutsu Kaisen S2",
        "studio": "MAPPA",
        "original_creator": "@gojovfx",
        "platform": "TikTok",
        "source_url": "https://www.tiktok.com/@gojovfx/video/12345"
      },
      {
        "rank": "1",
        "level": "Level 5",
        "anime_title": "Demon Slayer: Entertainment District",
        "studio": "ufotable",
        "original_creator": "@tengen_edits",
        "platform": "YouTube",
        "source_url": "https://youtube.com/shorts/abcdef"
      }
    ]
    print(build_youtube_description(test_sub, test_clips))
