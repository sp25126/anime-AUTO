import json

path = "src/pipeline/master_anime_registry.json"
with open(path, "r", encoding="utf-8") as f:
    reg = json.load(f)

# 1. Add Dynamic Auto-Discovery Subcategory for Single Anime Franchise
reg["subcategories"]["dynamic_booming_anime_isolation"] = {
    "title": "Dynamic Real-Time Booming Anime Franchise Ranking",
    "type": "dynamic_auto_discovery",
    "description": "Scans live YouTube virality trends to detect which anime is breaking out right now (e.g. Dandadan, Solo Leveling, Kaiju No. 8, Sakamoto Days), locks strictly into that single anime, and produces a 10-15s rank countdown.",
    "logic": "Real-time VPH (views per hour) & velocity scoring across YouTube API / scraping",
    "isolation": "Strict single franchise whitelist (zero cross-anime clips)",
    "duration_per_clip": "10-15s",
    "audio": "Native Japanese audio + original edit music"
}

# 2. Add Booming Viral Trends identified from YT Research
booming_trends = {
    "trending_phonk_bass_boost": {
        "title": "Top 5 Hardest Anime Phonk & Bass-Boosted Edits",
        "type": "audio_visual_trend",
        "description": "Rapid-fire aggressive phonk cuts, screen shakes, inverted color pulses, and heavy bass drops.",
        "target_audience": "Phonk & Gym motivation anime crowd"
    },
    "power_scaling_debate_edits": {
        "title": "Who Truly Wins? Peak Anime Power Scaling Clashes",
        "type": "debate_comparison",
        "description": "Versus battles (e.g. Gojo vs Sukuna, Sung Jinwoo vs Saitama) comparing feats, speed, and hax with comment debate triggers.",
        "target_audience": "Debate and vs-battle community"
    },
    "villain_cold_aura_walks": {
        "title": "Coldest Anime Villain Entrances & Aura Moments",
        "type": "character_archetype",
        "description": "Aizen, Toji, Sukuna, Madara, and Johan Liebert walking in while heroes freeze in terror.",
        "target_audience": "Aura and sigma anime edit fans"
    },
    "satisfying_sound_design_sakuga": {
        "title": "Most Ear-Pleasing Anime Sound Effects & Impact Frames",
        "type": "sound_and_animation",
        "description": "Heavy fire-force bass blasts, sword sheathing clicks, and razor-sharp impact frames with pure native SFX.",
        "target_audience": "Audiophile & animation sakuga enthusiasts"
    },
    "out_of_context_unhinged_moments": {
        "title": "Out of Context Anime Moments That Feel Illegal",
        "type": "humor_shock",
        "description": "Wild, bizarre, and out-of-context anime scenes cut with zero explanation right before the punchline.",
        "target_audience": "Mainstream casual meme audience"
    },
    "underrated_hidden_gem_breakouts": {
        "title": "Top 5 Insane Hidden Gem Anime Scenes Nobody Talks About",
        "type": "discovery_recommendation",
        "description": "Lesser-known anime with movie-level god-tier sakuga animation that shock the viewer.",
        "target_audience": "Curious anime watchers looking for fresh shows"
    }
}

for k, v in booming_trends.items():
    reg["subcategories"][k] = v

with open(path, "w", encoding="utf-8") as f:
    json.dump(reg, f, indent=2)

count = len(reg["subcategories"])
print(f"Registry updated! Total subcategories now: {count}")
