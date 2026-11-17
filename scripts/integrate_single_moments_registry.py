import json

reg_path = "src/pipeline/master_anime_registry.json"
with open(reg_path, "r", encoding="utf-8") as f:
    reg = json.load(f)

# Define the complete 20 single anime moment subcategories
single_moments = {
    "moment_accidental_rizz": {
        "title": "Accidental Rizz & Flustered Encounters",
        "type": "single_peak_anime_moment",
        "description": "An oblivious male lead says something completely straightforward, triggering extreme blushing and flustered reactions.",
        "hook_formula": "Bro Rizzed Them Without Even Knowing | [Anime]",
        "duration": "35-55s",
        "audio": "Native Japanese dialogue & authentic comedic timing"
    },
    "moment_hidden_power_flex": {
        "title": "The Undercover OP Protagonist Flex",
        "type": "single_peak_anime_moment",
        "description": "An undercover overpowered protagonist accidentally or casually reveals a fraction of god-tier power to shock everyone.",
        "hook_formula": "Bro Forgot He Was Supposed To Hide His Power | [Anime]",
        "duration": "40-60s",
        "audio": "Native Japanese dialogue & sudden power sound effects"
    },
    "moment_brutal_reality_check": {
        "title": "The Brutal Reality Check / Arrogance Crushed",
        "type": "single_peak_anime_moment",
        "description": "A cocky, overconfident character challenges an absolute monster and gets instantly shut down with zero effort.",
        "hook_formula": "The Exact Second He Realized He Messed Up 💀 | [Anime]",
        "duration": "30-45s",
        "audio": "Native dialogue with sudden shock silence"
    },
    "moment_character_rage_snap": {
        "title": "When The Gentle Character Finally Snaps",
        "type": "single_peak_anime_moment",
        "description": "A gentle or pacifist character watches someone cross the line. The smile fades and terrifying rage takes over.",
        "hook_formula": "The Moment The Calm Character Finally Snapped | [Anime]",
        "duration": "40-60s",
        "audio": "Tension silence followed by explosive battle roar"
    },
    "moment_cold_verbal_violation": {
        "title": "Coldest Verbal Disrespect & One-Liners",
        "type": "single_peak_anime_moment",
        "description": "Pure psychological destruction where a character destroys an opponent with a cold, dismissive verbal line.",
        "hook_formula": "Bro Didn't Have To Disrespect Him Like That 😭 | [Anime]",
        "duration": "25-40s",
        "audio": "Crisp voice acting with deep bass pause"
    },
    "moment_clutch_savior_arrival": {
        "title": "Peak Emotional Clutch Rescue (Savior Arrival)",
        "type": "single_peak_anime_moment",
        "description": "A character is on the brink of death; at the final millisecond, the protector arrives to deflect the fatal blow.",
        "hook_formula": "When All Hope Was Lost... HE ARRIVED 🥶 | [Anime]",
        "duration": "35-55s",
        "audio": "Heartbeat pause followed by epic orchestral arrival"
    },
    "moment_unhinged_comedy_gag": {
        "title": "Unhinged / Out-of-Context Deranged Gags",
        "type": "single_peak_anime_moment",
        "description": "Surreal, absurd anime moments where logic breaks down completely and characters act completely unhinged.",
        "hook_formula": "Anime Moments That Feel Completely Illegal 😂 | [Anime]",
        "duration": "20-40s",
        "audio": "Hilarious frantic voice acting and slapstick foley"
    },
    "moment_underdog_silences_crowd": {
        "title": "The Underdog Silences The Entire Crowd",
        "type": "single_peak_anime_moment",
        "description": "A mocked underdog shocks an entire arena or stadium into absolute dead silence with one decisive strike.",
        "hook_formula": "The Entire Stadium Went Dead Silent in 3 Seconds | [Anime]",
        "duration": "35-50s",
        "audio": "Crowd cheering cuts instantly to dead silence"
    },
    "moment_menacing_presence_walk": {
        "title": "The Unstoppable Walking Hazard Presence",
        "type": "single_peak_anime_moment",
        "description": "A monster character walks into the battlefield, forcing opponents to freeze, tremble, and drop their weapons.",
        "hook_formula": "Bro's Presence Alone Made Them Drop Their Weapons | [Anime]",
        "duration": "30-45s",
        "audio": "Heavy footsteps and menacing atmospheric rumble"
    },
    "moment_instant_technique_copy": {
        "title": "The Instant Master Technique Copy Flex",
        "type": "single_peak_anime_moment",
        "description": "An arrogant fighter demonstrates a secret technique, only for the genius protagonist to copy and master it instantly.",
        "hook_formula": "He Saw It ONCE And Perfected It Instantly ⚡ | [Anime]",
        "duration": "35-50s",
        "audio": "Detailed magical hum and shock gasps"
    },
    "moment_heartbreaking_body_shield": {
        "title": "The Heartbreaking Sacrificial Body Shield",
        "type": "single_peak_anime_moment",
        "description": "A mentor or friend throws their body in front of a fatal blow to protect someone, smiling through the pain.",
        "hook_formula": "His Body Moved On Its Own... 💔 | [Anime]",
        "duration": "40-60s",
        "audio": "Tearful voice acting and poignant silence"
    },
    "moment_mascot_true_form_reveal": {
        "title": "Harmless Pet Unleashes Colossal True Form",
        "type": "single_peak_anime_moment",
        "description": "Enemies mock a cute tiny mascot creature, until it suddenly awakens into an earth-shattering primordial beast.",
        "hook_formula": "They Thought It Was A Cute Pet Until It Transformed 😱 | [Anime]",
        "duration": "30-50s",
        "audio": "Cute squeaks shifting into colossal sub-bass roar"
    },
    "moment_touch_them_and_die": {
        "title": "The 'You Hurt My Loved One' Death Warrant",
        "type": "single_peak_anime_moment",
        "description": "A villain makes the fatal mistake of threatening or touching the protagonist's loved one, unleashing absolute carnage.",
        "hook_formula": "The Single Biggest Mistake In Anime History 💀 | [Anime]",
        "duration": "35-55s",
        "audio": "Desaturated audio silence before brutal beatdown"
    },
    "moment_stare_of_pure_death": {
        "title": "The Stare That Took 10 Years Off His Life",
        "type": "single_peak_anime_moment",
        "description": "A single menacing glance over the shoulder causes the opponent to hallucinate their own execution.",
        "hook_formula": "That One Stare Took 10 Years Off His Life 🥶 | [Anime]",
        "duration": "25-40s",
        "audio": "High-pitch tinnitus ringing and heartbeat pulse"
    },
    "moment_genius_bluff_success": {
        "title": "The 0% Plan, 100% Confidence Master Bluff",
        "type": "single_peak_anime_moment",
        "description": "A character has no idea what they are doing, but their deadpan poker face convinces the genius villain they are a mastermind.",
        "hook_formula": "0% Plan, But 100% Confidence and It WORKED 😂 | [Anime]",
        "duration": "30-45s",
        "audio": "Internal panic monologue mixed with cool exterior voice"
    },
    "moment_standing_on_pure_willpower": {
        "title": "The Undefeated Stand on Pure Willpower",
        "type": "single_peak_anime_moment",
        "description": "Despite suffering fatal injuries that should kill anyone, the legendary hero refuses to fall, terrifying the enemy.",
        "hook_formula": "Even In Death, He Refused To Fall 👑 | [Anime]",
        "duration": "40-60s",
        "audio": "Inspiring battle speech with heavy breathing"
    },
    "moment_holding_back_percentage_reveal": {
        "title": "The 'That Was Only 10% Power' Reality Drop",
        "type": "single_peak_anime_moment",
        "description": "The enemy celebrates surviving an intense attack, only for the boss to reveal they were barely using any power.",
        "hook_formula": "He Thought They Were Equal Until Bro Dropped This Line | [Anime]",
        "duration": "30-45s",
        "audio": "Arrogant calm speech over quiet bass tone"
    },
    "moment_cold_blood_revenge_execution": {
        "title": "The Cold-Blooded No-Mercy Revenge Execution",
        "type": "single_peak_anime_moment",
        "description": "The defeated villain begs for forgiveness or starts a speech, only to be eliminated instantly with zero hesitation.",
        "hook_formula": "Bro Did Not Let Him Finish His Villain Monologue 💀 | [Anime]",
        "duration": "25-40s",
        "audio": "Mid-sentence cutoff with clean decisive strike sound"
    },
    "moment_weapon_awakening_release": {
        "title": "First Legendary Weapon / Shikai Unsheathing",
        "type": "single_peak_anime_moment",
        "description": "A sealed ancient blade or cursed artifact is drawn for the first time, warping the atmosphere with insane visual effects.",
        "hook_formula": "The Sky Changed Color When He Unsheathed This Blade ⚔️ | [Anime]",
        "duration": "30-50s",
        "audio": "Metallic ring resonating with deep sub-bass pulse"
    },
    "moment_unspoken_mutual_respect": {
        "title": "The Unspoken Nod of Two Peak Monsters",
        "type": "single_peak_anime_moment",
        "description": "Two top-tier warriors make eye contact across a chaotic battlefield, acknowledging each other's strength without a word.",
        "hook_formula": "When Two Monsters Acknowledge Each Other Without A Word 🤝 | [Anime]",
        "duration": "25-40s",
        "audio": "Wind howling with subtle ambient theme swell"
    }
}

if "core_niches" not in reg:
    reg["core_niches"] = {}

reg["core_niches"]["single_peak_anime_moment"] = {
    "name": "Single Uncut Peak Anime Moments",
    "composition": "SingleMomentShort",
    "pacing": "25-60s (uncut narrative climax)",
    "visual_rules": {
        "title": "Contextual hook formula in title/metadata ([Bro / When / The Moment...] | [Anime])",
        "framing": "Original aspect ratio centered with dynamic blurred video background",
        "watermark": "Subtle 64x64 corner badge (@animefandom0_0) with zero sound effects",
        "credit": "Clean bottom attribution pill (CR: @creator / Studio)"
    }
}

for k, v in single_moments.items():
    reg["subcategories"][k] = v

with open(reg_path, "w", encoding="utf-8") as f:
    json.dump(reg, f, indent=2)

count = len(reg["subcategories"])
print(f"Successfully integrated all 20 Single Anime Moment subcategories into registry! Total active subcategories: {count}")
