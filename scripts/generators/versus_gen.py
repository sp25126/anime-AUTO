"""
Versus 1v1 Battle Cue Sheet Generator.
Takes two anime characters, fetches canonical stats and clips,
and formats cue_sheet_versus.json for Remotion rendering.
"""

import os
import sys
import json
import argparse
from typing import Dict, Any, List

WORKSPACE = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Preset benchmark battles
PRESET_BATTLES = {
    "gojo_vs_sukuna": {
        "char1Name": "SATORU GOJO",
        "char1Anime": "Jujutsu Kaisen",
        "char1VideoPath": "public/clips/gojo.mp4",
        "char2Name": "RYOMEN SUKUNA",
        "char2Anime": "Jujutsu Kaisen",
        "char2VideoPath": "public/clips/sukuna.mp4",
        "stats": [
            { "category": "PHYSICAL STRENGTH", "winner": "char2" },
            { "category": "TRAVEL & COMBAT SPEED", "winner": "char1" },
            { "category": "DURABILITY & HEALING", "winner": "char2" },
            { "category": "BATTLE IQ & TACTICS", "winner": "tie" },
            { "category": "HAX & INFINITY BARRIER", "winner": "char1" },
            { "category": "DOMAIN REFINEMENT", "winner": "char2" },
            { "category": "DESTRUCTIVE CAPACITY", "winner": "char2" }
        ],
        "overallWinner": "RYOMEN SUKUNA (EXTREME DIFF)",
        "audioPath": "public/audio/stems/versus_phonk_bed.mp3"
    },
    "jinwoo_vs_saitama": {
        "char1Name": "SUNG JINWOO",
        "char1Anime": "Solo Leveling",
        "char1VideoPath": "public/clips/jinwoo.mp4",
        "char2Name": "SAITAMA",
        "char2Anime": "One Punch Man",
        "char2VideoPath": "public/clips/saitama.mp4",
        "stats": [
            { "category": "RAW STRENGTH", "winner": "char2" },
            { "category": "COMBAT SPEED", "winner": "char2" },
            { "category": "ARMY SIZE (SHADOWS)", "winner": "char1" },
            { "category": "DIMENSIONAL TRAVEL", "winner": "char1" },
            { "category": "IMMORTALITY & REGEN", "winner": "char1" },
            { "category": "ATTACK POTENCY", "winner": "char2" },
            { "category": "DURABILITY", "winner": "char2" }
        ],
        "overallWinner": "SAITAMA (MID DIFF)",
        "audioPath": "public/audio/stems/versus_phonk_bed.mp3"
    },
    "eren_vs_kaneki": {
        "char1Name": "EREN YEAGER",
        "char1Anime": "Attack on Titan",
        "char1VideoPath": "public/clips/eren.mp4",
        "char2Name": "KEN KANEKI",
        "char2Anime": "Tokyo Ghoul",
        "char2VideoPath": "public/clips/kaneki.mp4",
        "stats": [
            { "category": "RAW SIZE & SCALE", "winner": "char1" },
            { "category": "SPEED & AGILITY", "winner": "char2" },
            { "category": "KAGUNE PIERCING POWER", "winner": "char2" },
            { "category": "COLOSSAL ARMY (RUMBLING)", "winner": "char1" },
            { "category": "BATTLE DETERMINATION", "winner": "tie" },
            { "category": "CLOSE COMBAT SKILL", "winner": "char2" },
            { "category": "TOTAL APOCALYPSE SCALE", "winner": "char1" }
        ],
        "overallWinner": "EREN YEAGER (WITH RUMBLING)",
        "audioPath": "public/audio/stems/versus_phonk_bed.mp3"
    }
}

def generate_versus_cue_sheet(battle_key: str = "gojo_vs_sukuna", output_path: str = None) -> Dict[str, Any]:
    battle = PRESET_BATTLES.get(battle_key, PRESET_BATTLES["gojo_vs_sukuna"])
    if not output_path:
        output_path = os.path.join(WORKSPACE, f"cue_sheet_versus_{battle_key}.json")
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(battle, f, indent=2)
        
    print(f"[VersusGen] Generated cue sheet: {output_path}")
    print(f" -> Battle: {battle['char1Name']} vs {battle['char2Name']}")
    print(f" -> Projected Winner: {battle['overallWinner']}")
    return battle

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--battle", type=str, default="gojo_vs_sukuna")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()
    
    generate_versus_cue_sheet(args.battle, args.output)
