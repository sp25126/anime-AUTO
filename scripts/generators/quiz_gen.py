"""
Interactive Anime Quiz Cue Sheet Generator.
Generates 3-second challenge cues (blurred silhouette / eyes / weapon teaser)
with timed answer reveals and engagement prompts for YouTube Shorts.
"""

import os
import sys
import json
import argparse
from typing import Dict, Any

WORKSPACE = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

QUIZ_BANK = [
    {
        "id": "quiz_gojo_eyes",
        "quizPrompt": "GUESS THE ANIME IN 3 SECONDS",
        "characterName": "Satoru Gojo (Six Eyes)",
        "animeAnswer": "JUJUTSU KAISEN",
        "revealVideoPath": "temp_harvest/yt_dIvAk_VlM3s.mp4",
        "audioPath": "public/audio/stems/quiz_timer_bed.mp3",
        "timerSeconds": 3
    },
    {
        "id": "quiz_sukuna_domain",
        "quizPrompt": "GUESS THE DOMAIN EXPANSION",
        "characterName": "Ryomen Sukuna",
        "animeAnswer": "MALEVOLENT SHRINE",
        "revealVideoPath": "temp_harvest/yt_YD3FZ7Gr3fI.mp4",
        "audioPath": "public/audio/stems/quiz_timer_bed.mp3",
        "timerSeconds": 3
    },
    {
        "id": "quiz_tengen_uzui",
        "quizPrompt": "GUESS THE HASHIRA IN 3 SECONDS",
        "characterName": "Tengen Uzui (Sound Hashira)",
        "animeAnswer": "DEMON SLAYER",
        "revealVideoPath": "public/clips/tengen.mp4",
        "audioPath": "public/audio/stems/quiz_timer_bed.mp3",
        "timerSeconds": 3
    }
]

def generate_quiz_cue_sheet(quiz_id: str = "quiz_gojo_eyes", output_path: str = None) -> Dict[str, Any]:
    quiz = next((q for q in QUIZ_BANK if q["id"] == quiz_id), QUIZ_BANK[0])
    if not output_path:
        output_path = os.path.join(WORKSPACE, f"cue_sheet_{quiz_id}.json")
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(quiz, f, indent=2)
        
    print(f"[QuizGen] Generated quiz cue sheet: {output_path}")
    print(f" -> Question: '{quiz['quizPrompt']}'")
    print(f" -> Secret Answer: {quiz['animeAnswer']} ({quiz['characterName']})")
    return quiz

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=str, default="quiz_gojo_eyes")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()
    
    generate_quiz_cue_sheet(args.id, args.output)
