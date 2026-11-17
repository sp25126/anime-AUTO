"""
Viral Trend & Cross-Anime Audio-Visual Theme Catalog
Covers:
- Trending Songs & BGM Hooks (Phonk, Brazilian Funk, Jersey Club, Lo-Fi Rizz, Orchestral Chills)
- Cross-Anime Viral Tropes (Coldest Aura, Awakening Rage, Swordsman Clashes, Hand-To-Hand, Accidental Rizz, Brutal Reality Checks)
- Multi-Franchise Crossover Compilations (Not tied to a single anime)
"""

VIRAL_THEMES = {
    # -------------------------------------------------------------
    # GROUP A: MULTI-CLIP RANKING COMPILATIONS (75-80s)
    # Driven by trending themes, sounds, and tropes across multiple anime
    # -------------------------------------------------------------
    "ranking_coldest_aura": {
        "group": "GROUP_A",
        "theme_name": "Coldest 1,000,000+ Aura Walks in Anime",
        "title_template": "Top 5 COLDEST Anime Aura Walks That Broke The Internet! 💀🥶 #shorts #anime",
        "search_queries": [
            "top 5 anime cold aura walks edit shorts",
            "coldest anime villain walk phonk edit",
            "anime characters with 1000000 aura edit",
            "anime walking menacingly edit 4k"
        ],
        "bgm_style": "phonk_drift_bass",
        "clip_archetypes": ["Aizen chair walk", "Madara shinobi army walk", "Toji stroll", "Gojo confident walk", "Gilgamesh golden gate walk"],
        "tags": ["aura", "coldest aura", "anime villains", "toji", "madara", "aizen", "gojo", "phonk", "shorts"]
    },
    "ranking_hardest_beat_drops": {
        "group": "GROUP_A",
        "theme_name": "Hardest Anime Beat Drops & Speed Ramps",
        "title_template": "Top 5 HARDEST Anime Beat Drops on TikTok & YouTube! 🔥🔊 #shorts #animeedit",
        "search_queries": [
            "top 5 anime beat drops edit 4k",
            "hardest anime phonk beat drop shorts",
            "anime edit sync beat drop 60fps",
            "best anime velocity edit shorts"
        ],
        "bgm_style": "brazilian_phonk_funk",
        "clip_archetypes": ["Sukuna flame arrow", "Asta black divider", "Jinwoo arise", "Luffy gear 5 laugh", "Zenitsu godspeed"],
        "tags": ["beat drop", "anime phonk", "sync", "velocity", "alight motion", "capcut", "shorts"]
    },
    "ranking_pure_rage_awakenings": {
        "group": "GROUP_A",
        "theme_name": "Pure Uncontrolled Rage Awakening Moments",
        "title_template": "Top 5 Anime Characters Who Lost All Control & Snapped! 👹⚡ #shorts #anime",
        "search_queries": [
            "top 5 anime rage awakening moments edit",
            "anime characters losing control edit 4k",
            "pure rage anime moments shorts",
            "gon rage vs pitou edit 4k"
        ],
        "bgm_style": "orchestral_dark_trap",
        "clip_archetypes": ["Gon transformation", "Mob 100% rage", "Tanjiro sun breathing rage", "Eren founding scream", "Naruto 4 tails"],
        "tags": ["anime rage", "awakening", "gon", "mob psycho", "eren", "tanjiro", "hype", "shorts"]
    },
    "ranking_swordsman_clashes": {
        "group": "GROUP_A",
        "theme_name": "Greatest Swordsman Clashes & Blade Draws",
        "title_template": "Top 5 Coldest Swordsman Clashes in Anime History! ⚔️🔥 #shorts #anime",
        "search_queries": [
            "top 5 anime swordsman clashes edit",
            "best anime katana fight scenes 4k",
            "satisfying anime sword sound design shorts",
            "zoro vs king 4k edit short"
        ],
        "bgm_style": "katana_phonk_sfx",
        "clip_archetypes": ["Zoro King of Hell", "Atomic Samurai slash", "Yoriichi demon slayer", "Rengoku Akaza", "Ichigo getsuga"],
        "tags": ["swordsman", "katana", "zoro", "rengoku", "ichigo", "yoriichi", "sakuga", "shorts"]
    },
    "ranking_hand_to_hand_combat": {
        "group": "GROUP_A",
        "theme_name": "Best Hand-to-Hand Martial Arts Fights",
        "title_template": "Top 5 Insane Hand-to-Hand Fights in Anime! 🥋💥 #shorts #animeedit",
        "search_queries": [
            "top 5 anime hand to hand combat edit",
            "best taijutsu fights anime 4k short",
            "kakashi vs obito 4k edit short",
            "satisfying martial arts anime edit"
        ],
        "bgm_style": "punch_heavy_phonk",
        "clip_archetypes": ["Kakashi vs Obito", "Yuji & Todo vs Hanami", "Garou martial arts", "Mori Jin", "Chunjie"],
        "tags": ["taijutsu", "hand to hand", "kakashi", "obito", "yuji", "garou", "fight", "shorts"]
    },

    # -------------------------------------------------------------
    # GROUP B: ROTATE YOUR PHONE CINEMATIC AMVS (30s)
    # Driven by viral trending songs + panoramic widescreen sakuga
    # -------------------------------------------------------------
    "rotate_slava_phonk": {
        "group": "GROUP_B",
        "theme_name": "Trending Phonk: Slava Funk / Montagem",
        "title_template": "ROTATE YOUR PHONE for the Hardest Phonk Battle Edit! 📱🔄⚡ #shorts #animeedit",
        "search_queries": [
            "solo leveling slava funk 4k amv 60fps",
            "sukuna vs mahoraga slava funk 4k amv",
            "demon slayer infinity castle phonk 4k amv"
        ],
        "trending_song": "SLAVA FUNK / Montagem",
        "tags": ["rotate your phone", "phonk", "amv", "4k 60fps", "sukuna", "jinwoo", "demon slayer", "shorts"]
    },
    "rotate_timeless_guitar": {
        "group": "GROUP_B",
        "theme_name": "Trending Audio: Timeless Guitar Remix / Memory Reboot",
        "title_template": "ROTATE YOUR PHONE for Chills! (Peak Cinema) 📱🔄✨ #shorts #animeedit",
        "search_queries": [
            "demon slayer timeless guitar 4k amv",
            "memory reboot anime 4k amv 60fps",
            "frieren vs clone 4k amv 60fps",
            "bleach tybw senbonzakura 4k amv 60fps"
        ],
        "trending_song": "Timeless Guitar / Memory Reboot",
        "tags": ["rotate your phone", "timeless", "memory reboot", "chills", "frieren", "bleach", "shorts"]
    },
    "rotate_drums_of_liberation": {
        "group": "GROUP_B",
        "theme_name": "Trending Sound: Drums of Liberation / Phonk Remix",
        "title_template": "ROTATE YOUR PHONE for the Drums of Liberation! 📱🔄🥁 #shorts #animeedit",
        "search_queries": [
            "luffy gear 5 drums of liberation 4k amv 60fps",
            "gear 5 joyboy phonk 4k 60fps amv",
            "one piece wano climax 4k amv"
        ],
        "trending_song": "Drums of Liberation Joyboy",
        "tags": ["rotate your phone", "gear 5", "joyboy", "luffy", "one piece", "4k 60fps", "shorts"]
    },

    # -------------------------------------------------------------
    # GROUP C: VIRAL MICRO-MOMENTS & COMEDY GAGS (25-35s)
    # Driven by trending social audio tropes (Accidental Rizz, Brutal Honesty, Deadpan Pauses)
    # -------------------------------------------------------------
    "moment_accidental_rizz": {
        "group": "GROUP_C",
        "theme_name": "Accidental Rizz & Flustered Encounters",
        "title_template": "Bro Rizzed Her Without Even Realizing 😭💀 #shorts #anime",
        "search_queries": [
            "anime accidental rizz moments english sub",
            "oblivious anime mc rizz funny moment",
            "anime female lead blushing flustered funny moment",
            "dandadan okarun accidental rizz english sub"
        ],
        "trending_trope": "Accidental Rizz",
        "tags": ["accidental rizz", "rizz", "funny anime", "romcom", "dandadan", "okarun", "momo", "shorts"]
    },
    "moment_brutal_reality_check": {
        "group": "GROUP_C",
        "theme_name": "Brutal Reality Checks & Emotional Violations",
        "title_template": "He Really Didn't Hesitate For A Second 💀😂 #shorts #anime",
        "search_queries": [
            "anime brutal reality check english sub",
            "anime emotional damage moments english sub",
            "anime cold verbal violation funny moment",
            "anime deadpan response funny moments sub"
        ],
        "trending_trope": "Brutal Reality Check",
        "tags": ["emotional damage", "brutal reality check", "didn't hesitate", "funny anime", "comedy", "shorts"]
    },
    "moment_unhinged_comedy": {
        "group": "GROUP_C",
        "theme_name": "Pure Unhinged Comedy & Chaotic Banter",
        "title_template": "These Two Have Zero Filter 🤣💀 #shorts #anime",
        "search_queries": [
            "unhinged anime comedy moments english sub",
            "anime chaotic duo funny moments sub",
            "konosuba unhinged moments sub",
            "gintama funniest moments english sub"
        ],
        "trending_trope": "Zero Filter Banter",
        "tags": ["anime comedy", "chaotic duo", "unhinged", "funny anime", "konosuba", "gintama", "shorts"]
    }
}
