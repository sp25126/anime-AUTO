"""
Anime Lore & Theory Explainer Generator.
Formats explainer cue sheets with hook titles, topic tags,
video b-roll paths, and word-by-word kinetic subtitle timings.
"""

import os
import sys
import json
import argparse
from typing import Dict, Any

WORKSPACE = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

EXPLAINER_BANK = [
    {
        "id": "explainer_gojo_blindfold",
        "hookTitle": "WHY GOJO WEARS A BLINDFOLD",
        "topicSubject": "Jujutsu Kaisen Dark Lore",
        "videoPath": "temp_harvest/yt_zmrp_RH4OfU.mp4",
        "backgroundMusicPath": "public/audio/stems/explainer_ambient_bed.mp3",
        "captions": [
            { "word": "Most", "startFrame": 0, "endFrame": 15 },
            { "word": "fans", "startFrame": 15, "endFrame": 30 },
            { "word": "think", "startFrame": 30, "endFrame": 45 },
            { "word": "Gojo", "startFrame": 45, "endFrame": 65 },
            { "word": "wears", "startFrame": 65, "endFrame": 80 },
            { "word": "a", "startFrame": 80, "endFrame": 90 },
            { "word": "blindfold", "startFrame": 90, "endFrame": 115 },
            { "word": "to", "startFrame": 115, "endFrame": 125 },
            { "word": "look", "startFrame": 125, "endFrame": 140 },
            { "word": "cool...", "startFrame": 140, "endFrame": 170 },
            { "word": "BUT", "startFrame": 170, "endFrame": 195 },
            { "word": "THE", "startFrame": 195, "endFrame": 215 },
            { "word": "TRUTH", "startFrame": 215, "endFrame": 240 },
            { "word": "IS", "startFrame": 240, "endFrame": 260 },
            { "word": "TERRIFYING.", "startFrame": 260, "endFrame": 310 }
        ]
    },
    {
        "id": "explainer_sukuna_fingers",
        "hookTitle": "THE CURSE OF SUKUNA'S FINGERS",
        "topicSubject": "Heian Era Mysteries",
        "videoPath": "temp_harvest/yt_YD3FZ7Gr3fI.mp4",
        "backgroundMusicPath": "public/audio/stems/explainer_ambient_bed.mp3",
        "captions": [
            { "word": "In", "startFrame": 0, "endFrame": 15 },
            { "word": "the", "startFrame": 15, "endFrame": 25 },
            { "word": "Heian", "startFrame": 25, "endFrame": 45 },
            { "word": "Era,", "startFrame": 45, "endFrame": 65 },
            { "word": "sorcerers", "startFrame": 65, "endFrame": 95 },
            { "word": "could", "startFrame": 95, "endFrame": 110 },
            { "word": "NOT", "startFrame": 110, "endFrame": 135 },
            { "word": "destroy", "startFrame": 135, "endFrame": 165 },
            { "word": "Sukuna's", "startFrame": 165, "endFrame": 200 },
            { "word": "remains...", "startFrame": 200, "endFrame": 240 }
        ]
    }
]

def generate_explainer_cue_sheet(explainer_id: str = "explainer_gojo_blindfold", output_path: str = None) -> Dict[str, Any]:
    item = next((e for e in EXPLAINER_BANK if e["id"] == explainer_id), EXPLAINER_BANK[0])
    if not output_path:
        output_path = os.path.join(WORKSPACE, f"cue_sheet_{explainer_id}.json")
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(item, f, indent=2)
        
    print(f"[ExplainerGen] Generated explainer cue sheet: {output_path}")
    print(f" -> Hook: \"{item['hookTitle']}\" ({item['topicSubject']})")
    print(f" -> Captions count: {len(item['captions'])} words mapped")
    return item

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=str, default="explainer_gojo_blindfold")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()
    
    generate_explainer_cue_sheet(args.id, args.output)
