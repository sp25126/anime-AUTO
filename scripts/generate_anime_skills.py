"""
Generates reusable production-grade Sub-Category Skills in subcategory_skills/
for all 20 anime subcategories matching the battle-tested format from b8fda61d-805e-472a-8bf8-5304771d90af.
Includes multi-platform queries, 5-clip benchmark ladder, and strict credit attribution templates.
"""

import os
import json

WORKSPACE = os.path.dirname(os.path.dirname(__file__))
SKILLS_DIR = os.path.join(WORKSPACE, "subcategory_skills")
os.makedirs(SKILLS_DIR, exist_ok=True)

REGISTRY_PATH = os.path.join(WORKSPACE, "src", "pipeline", "master_anime_registry.json")
with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
    master_registry = json.load(f)

ALL_20_SPECS = [
    {
        "id": "trending_anime_edits",
        "name": "TRENDING VIRAL ANIME EDITS",
        "focus": "Viral Velocity, Twixtor Flow & Phonk Transitions",
        "title": "Ranking Trending",
        "subject": "VIRAL ANIME EDITS",
        "version": "(Peak Flow Edition)",
        "hook_title": "Ranking Trending Viral Anime Edits 🔥⚡ #shorts #anime #animeedit",
        "audio_stem": "public/audio/stems/trending_anime_edits_bed.mp3",
        "audio_source": "PLAYAMANE & Nateki - MIDNIGHT (Phonk Velocity Remix)",
        "audio_bg_vol": 0.12,
        "story_arc": "Subtle character aura buildup -> High-speed twixtor/velocity ramp -> Frame-perfect bass drop sync on combat strike or eye flare.",
        "requires_creator_credit": True,
        "ranks": [
            ("5", "Level 1", "Chainsaw Man - Aki Fox Devil Walkout", "@akivfx (TikTok)", "Aki makes hand sign -> 'Kon' whisper -> Massive fox jaw devours leech devil on bass drop.", "1.0s / 4.5s", "45", "FOX DEVIL SUMMON"),
            ("4", "Level 2", "Bleach TYBW - Yamamoto Bankai Flame", "@ichigo_flow (YouTube)", "Yamamoto lifts cracked sword -> Heat distortion incinerates raindrops -> Zanka no Tachi ignition.", "0.0s / 5.0s", "65", "ZANKA NO TACHI"),
            ("3", "Level 3", "Jujutsu Kaisen S2 - Toji Speed Blitz", "@zenin_edits (Instagram)", "Toji dashes across water surface -> Water droplets suspend in slow motion -> Sudden velocity strike.", "0.5s / 5.2s", "80", "ZERO CURSED ENERGY"),
            ("2", "Level 4", "Demon Slayer - Tengen vs Gyutaro Climax", "@soundhashira (TikTok)", "Dual cleavers spinning with spark trails -> Score drops to dead silence -> Musical score blast.", "1.2s / 6.0s", "110", "MUSICAL SCORE TECHNIQUE"),
            ("1", "Level 5", "One Piece - Luffy Gear 5 Lightning Grab", "@joyboy_vfx (YouTube)", "Luffy bounces on clouds laughing -> Grabs lightning bolt from thundercloud -> Divine slam impact.", "0.0s / 7.5s", "135", "WARRIOR OF LIBERATION")
        ]
    },
    {
        "id": "best_anime_by_genre",
        "name": "BEST ANIME IN EVERY GENRE",
        "focus": "Definitive Champions Across Shonen, Seinen, Romance, Isekai & Dark Fantasy",
        "title": "Ranking The Best Anime",
        "subject": "IN EVERY SINGLE GENRE",
        "version": "(Ultimate Tier)",
        "hook_title": "Ranking The Undisputed Best Anime In Every Genre 🏆 #shorts #anime #animerecommendations",
        "audio_stem": "public/audio/stems/best_anime_by_genre_bed.mp3",
        "audio_source": "Hiroyuki Sawano - YouSeeBIGGIRL/T:T (Epic Hybrid Remaster)",
        "audio_bg_vol": 0.14,
        "story_arc": "Establishment of the genre titan -> Signature emotional or combat climax -> Crowd-agreed supremacy badge.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "Romance: Kaguya-sama: Love Is War", "A-1 Pictures", "Miyuki & Kaguya mind games reach fever pitch -> Dual internal monologues explode with comic fireworks.", "0.0s / 4.2s", "50", "PEAK ROM-COM"),
            ("4", "Level 2", "Isekai: Re:Zero Season 2", "White Fox", "Subaru confronts the Witches of Sin -> Melancholic pledge to defy fate.", "1.0s / 5.0s", "70", "DESPAIR TRANSCENDED"),
            ("3", "Level 3", "Dark Fantasy: Berserk (1997 / Memorial)", "OLM / Studio 4°C", "Guts swings Dragonslayer in pouring rain -> Blood-curdling mercenary vow.", "0.5s / 5.5s", "90", "STRUGGLER'S PATH"),
            ("2", "Level 4", "Seinen: Vinland Saga Season 2", "MAPPA", "Thorfinn takes 100 punches without striking back -> 'I have no enemies' declaration.", "0.0s / 6.5s", "120", "I HAVE NO ENEMIES"),
            ("1", "Level 5", "Shonen: Hunter x Hunter (Chimera Ant)", "Madhouse", "Gon's final aura transformation in pitch black forest -> Tear falls on Nen explosion.", "0.0s / 8.0s", "140", "TRANSCENDENT NEN")
        ]
    },
    {
        "id": "anime_by_year_all_time",
        "name": "ANIME BY YEAR (GOLDEN ERA)",
        "focus": "Landmark Show of Each Year (2015-2025)",
        "title": "The #1 Anime From",
        "subject": "EVERY SINGLE YEAR",
        "version": "(2015 - 2025)",
        "hook_title": "The #1 Anime From Every Year (2015-2025) ⏳🔥 #shorts #anime #animeevolution",
        "audio_stem": "public/audio/stems/anime_by_year_bed.mp3",
        "audio_source": "Kavinsky & The Weeknd - Odd Look (Cyberpunk Riser Edit)",
        "audio_bg_vol": 0.13,
        "story_arc": "Chronological year jump -> Visual signature representing that calendar year -> Landmark cultural impact.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "2016: Re:Zero / Your Name", "White Fox / CoMix Wave", "Rem's confession under sunset / Comet split across Tokyo night sky.", "0.0s / 4.0s", "45", "2016 LANDMARK"),
            ("4", "Level 2", "2019: Demon Slayer (Ep 19 Hinokami)", "ufotable", "Tanjiro ignites Hinokami Kagura dance -> Nezuko Blood Demon Art triggers.", "0.0s / 5.0s", "65", "2019 INTERNET BREAK"),
            ("3", "Level 3", "2021: Attack on Titan Final Season", "MAPPA", "Eren transforms underneath Willy Tybur's stage in Liberio.", "0.0s / 5.5s", "85", "2021 DECLARATION OF WAR"),
            ("2", "Level 4", "2023: Jujutsu Kaisen S2 (Shibuya Arc)", "MAPPA", "Sukuna Malevolent Shrine domain expansion unfolds over Shibuya.", "0.5s / 6.2s", "110", "2023 SHIBUYA INCIDENT"),
            ("1", "Level 5", "2024: Frieren: Beyond Journey's End", "Madhouse", "Frieren reveals mana restriction against Aura the Guillotine -> 'Aura, kill yourself'.", "0.0s / 7.8s", "130", "2024 SUPREME MASTERPIECE")
        ]
    },
    {
        "id": "underrated_hidden_gems",
        "name": "UNDERRATED HIDDEN GEMS",
        "focus": "High Rating (>8.1) Slept-on Masterpieces",
        "title": "5 Masterpiece Anime",
        "subject": "NOBODY EVER TALKED ABOUT",
        "version": "(Hidden Gems)",
        "hook_title": "5 Anime Masterpieces That Nobody Talked About 💎✨ #shorts #underratedanime #hiddengem",
        "audio_stem": "public/audio/stems/underrated_gems_bed.mp3",
        "audio_source": "Kudasaibeats - The Girl I Haven't Met (Moody Lofi Trap)",
        "audio_bg_vol": 0.11,
        "story_arc": "Introduction of obscure title -> High-concept aesthetic hook -> Critical acclaim reveal.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "Odd Taxi", "OLM / P.I.C.S.", "Walrus taxi driver delivers deadpan cynical observation on nocturnal Tokyo.", "0.0s / 4.5s", "55", "CINEMATIC NOIR"),
            ("4", "Level 2", "Vivy: Fluorite Eye's Song", "Wit Studio", "AI diva transforms into martial arts assassin in neon android corridor.", "0.5s / 5.0s", "75", "WIT STUDIO SAKUGA"),
            ("3", "Level 3", "Summertime Render", "OLM", "Shinpei realizes shadow loop mechanics on sunny island dock.", "0.0s / 5.2s", "80", "TIME LOOP THRILLER"),
            ("2", "Level 4", "Dororo", "MAPPA", "Hyakkimaru slices demon in wheat field, regains vocal cords.", "0.0s / 6.0s", "100", "SOUL RECLAMATION"),
            ("1", "Level 5", "Land of the Lustrous (Houseki no Kuni)", "Orange", "Phosphophyllite combines gold alloys in moon battle, fluid CG marvel.", "0.0s / 7.0s", "125", "3D CGI MASTERPIECE")
        ]
    },
    {
        "id": "genre_by_year_cross_axis",
        "name": "GENRE BY YEAR (CROSS-AXIS)",
        "focus": "Best of Single Genre Across Consecutive Years",
        "title": "Best Isekai Anime",
        "subject": "BY YEAR EVOLUTION",
        "version": "(2018 - 2024)",
        "hook_title": "Best Isekai Anime By Year (2018-2024) 👑 #shorts #isekai #anime",
        "audio_stem": "public/audio/stems/genre_year_bed.mp3",
        "audio_source": "Myth & Roid - VORACITY (Hyper J-Rock Remix)",
        "audio_bg_vol": 0.14,
        "story_arc": "Annual evolution of genre tropes -> Progression from parody to peak high fantasy -> Definitive annual champion.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "2018: That Time I Got Reincarnated as a Slime", "8bit", "Rimuru devours dragon Veldora -> Magicule aura awakens.", "0.0s / 4.5s", "50", "2018 SLIME REVOLUTION"),
            ("4", "Level 2", "2020: Re:Zero Season 2", "White Fox", "Subaru confronts Echidna at tea party of greed.", "0.0s / 5.0s", "70", "2020 GREED TRIAL"),
            ("3", "Level 3", "2021: Mushoku Tensei: Jobless Reincarnation S1", "Studio Bind", "Rudy casts water cannon under Roxy's guidance with filmic camera movement.", "0.0s / 5.5s", "90", "2021 PEAK PRODUCTION"),
            ("2", "Level 4", "2022: The Eminence in Shadow", "Nexus", "Cid atomic blast vaporizes city core with classical music.", "0.0s / 6.2s", "110", "2022 CHUNIBYO GOD"),
            ("1", "Level 5", "2024: Mushoku Tensei S2 Part 2", "Studio Bind", "Labyrinth hydra battle with sacrificial spell casting.", "0.0s / 7.5s", "135", "2024 EMOTIONAL PEAK")
        ]
    },
    {
        "id": "anime_edits_sakuga_compilation",
        "name": "PEAK SAKUGA ANIMATION",
        "focus": "Fluid Keyframe Animation & Smear Frame Combat",
        "title": "Moments Where The",
        "subject": "ANIMATION BUDGET BROKE",
        "version": "(Pure Sakuga)",
        "hook_title": "Moments Where The Animation Budget Exploded 🤯💥 #shorts #sakuga #anime #animation",
        "audio_stem": "public/audio/stems/sakuga_compilation_bed.mp3",
        "audio_source": "DVRST - Close Eyes (Ultra Bass Boosted Sakuga Cut)",
        "audio_bg_vol": 0.13,
        "story_arc": "Combatants square up -> Hand-drawn kinetic smear lines & perspective shift -> Massive visual impact.",
        "requires_creator_credit": True,
        "ranks": [
            ("5", "Level 1", "Mob Psycho 100 - Shimazaki Fight", "Studio Bones (Animator: Kenichi Hakuno)", "Mob's esper circle wraps 360 degrees around building rooftop with pure hand-drawn debris.", "0.0s / 4.5s", "50", "BONES DEBRIS PHYSICS"),
            ("4", "Level 2", "Fate/Heaven's Feel - Saber Alter vs Berserker", "ufotable (Animator: Nozomu Abe)", "Excalibur Morgan beam cuts through forest with explosive volumetric fluid sparks.", "0.2s / 5.2s", "75", "UFOTABLE VOLUMETRIC VFX"),
            ("3", "Level 3", "One Punch Man S1 - Saitama vs Boros", "Madhouse (Animator: Arifumi Imai)", "Boros meteoric burst kicks Saitama to the moon, earth-bending scale.", "0.0s / 5.5s", "90", "METEORIC BURST"),
            ("2", "Level 4", "Jujutsu Kaisen S2 - Mahoraga vs Sukuna", "MAPPA (Animators: Tsuchigami & Team)", "City-level devastation with morphing abstract camera lines and relentless speed.", "0.0s / 6.5s", "115", "APOCALYPTIC SAKUGA"),
            ("1", "Level 5", "Sword of the Stranger - Final Snow Battle", "Studio Bones (Animator: Yutaka Nakamura)", "Nanashi unsheathes katana against Luo-Lang; legendary square cubes and smear choreography.", "0.0s / 8.0s", "145", "GOD TIER CHOREOGRAPHY")
        ]
    },
    {
        "id": "best_upcoming_anime_hype",
        "name": "BEST UPCOMING ANIME",
        "focus": "Anticipated New Seasons & Massive Premieres",
        "title": "Ranking The Most",
        "subject": "ANTICIPATED UPCOMING ANIME",
        "version": "(2025 Hype Tier)",
        "hook_title": "Most Anticipated Upcoming Anime Releasing In 2025 🚀🔥 #shorts #upcominganime #anime2025",
        "audio_stem": "public/audio/stems/upcoming_hype_bed.mp3",
        "audio_source": "2WEI & Ali Christenhusz - Crimson Wings (Trailer Impact)",
        "audio_bg_vol": 0.13,
        "story_arc": "Official announcement trailer reveal -> Escalating worldwide fandom excitement -> Release window countdown.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "Fire Force Season 3", "David Production", "Shinra and Arthur flame ignition teaser with bass-drop kicks.", "0.0s / 4.2s", "45", "FINAL FIRE DISASTER"),
            ("4", "Level 2", "Jujutsu Kaisen: Culling Game", "MAPPA", "Kenjaku introduces Culling Game rules across Tokyo barrier.", "0.0s / 5.0s", "65", "CULLING GAME BEGINS"),
            ("3", "Level 3", "Chainsaw Man: Reze Movie", "MAPPA", "Reze detonates explosive choke collar under festival fireworks.", "0.0s / 5.5s", "85", "BOMB DEVIL AWAKENS"),
            ("2", "Level 4", "Demon Slayer: Infinity Castle Arc Movie 1", "ufotable", "Hashira plunge through dimensional doors into the infinite fortress.", "0.0s / 6.5s", "110", "INFINITY CASTLE DESCENT"),
            ("1", "Level 5", "One-Punch Man Season 3", "J.C. Staff / Bandai", "Garou awakens monster forms against Orochi in underground labyrinth.", "0.0s / 7.8s", "135", "HUMAN MONSTER GAROU")
        ]
    },
    {
        "id": "best_anime_openings_ost",
        "name": "BEST ANIME OPENINGS & OST",
        "focus": "10/10 Legendary Song Drops & Chorus Peaks",
        "title": "Anime Openings That",
        "subject": "ARE AN ABSOLUTE 10/10",
        "version": "(Never Skip)",
        "hook_title": "Anime Openings That Are Literal 10/10 Masterpieces 🎧🔥 #shorts #animeop #animeost",
        "audio_stem": "public/audio/stems/openings_ost_bed.mp3",
        "audio_source": "TK from Ling Tosite Sigure - Unravel / Kenshi Yonezu - Kick Back",
        "audio_bg_vol": 0.20,
        "story_arc": "Iconic opening guitar riff / vocal intro -> Visual countdown -> Chorus drop with bass slam.",
        "requires_creator_credit": True,
        "ranks": [
            ("5", "Level 1", "Chainsaw Man: KICK BACK (Kenshi Yonezu)", "MAPPA / SME", "Denji pulls ripcord on chorus drop as devil hunters sprint through cinematic homage frames.", "0.0s / 4.5s", "55", "NEVER SKIP OP"),
            ("4", "Level 2", "Jujutsu Kaisen S2: SPECIALZ (King Gnu)", "MAPPA / Ariola", "Red neon Shibuya streets pulse in time with bassline walkout.", "0.0s / 5.0s", "70", "YOU ARE MY SPECIAL"),
            ("3", "Level 3", "Attack on Titan: The Rumbling (SiM)", "MAPPA / Pony Canyon", "Eren walks forward as Colossal Titans break through wall in metal breakdown.", "0.0s / 5.5s", "90", "WALL TITANS MARCH"),
            ("2", "Level 4", "Demon Slayer: Gurenge (LiSA)", "ufotable / SACRA MUSIC", "Water breathing kata transitions into flame sword slash on chorus blast.", "0.0s / 6.2s", "110", "ICONIC J-ROCK CHORUS"),
            ("1", "Level 5", "Tokyo Ghoul: Unravel (TK)", "Studio Pierrot / Sony", "Kaneki's eye turns red under shattered glass sky, unforgettable falsetto scream.", "0.0s / 7.5s", "135", "HISTORIC ANIME ANTHEM")
        ]
    },
    {
        "id": "iconic_transformations",
        "name": "ICONIC TRANSFORMATIONS",
        "focus": "God Form Awakenings & Internet-Breaking Forms",
        "title": "Anime Transformations That",
        "subject": "BROKE THE INTERNET",
        "version": "(God Form Edition)",
        "hook_title": "Anime Transformations That Broke The Entire Internet ⚡😱 #shorts #transformation #anime",
        "audio_stem": "public/audio/stems/transformations_bed.mp3",
        "audio_source": "Norihito Sumitomo - Ultimate Battle (Ka Ka Kachi Daze Remix)",
        "audio_bg_vol": 0.15,
        "story_arc": "Desperate cornered protagonist -> Riser heartbeat & eye flash -> Screaming aura release that shatters landscape.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "Bleach - Ichigo Hollow Mask First Appearance", "Studio Pierrot", "Byakuya prepares Senbonzakura -> Hollow mask locks over Ichigo's face with black Getsuga.", "0.0s / 4.5s", "50", "HOLLOWFICATION"),
            ("4", "Level 2", "Dragon Ball Super - Goku Ultra Instinct Sign", "Toei Animation", "Goku emerges from spirit bomb crater surrounded by silver heat ripples.", "0.0s / 5.2s", "75", "GODLY HEAT"),
            ("3", "Level 3", "Hunter x Hunter - Adult Gon Transformation", "Madhouse", "Pitou watches in terror as Gon's nen blackens the sky, hair reaching ceiling.", "0.0s / 6.0s", "95", "COVENANT PLEDGE"),
            ("2", "Level 4", "Attack on Titan - Eren First Rogue Titan Transformation", "Wit Studio", "Santa titan swallows Eren -> Arm bursts from mouth in lightning bolt.", "0.0s / 6.5s", "115", "ATTACK TITAN BORN"),
            ("1", "Level 5", "One Piece - Luffy Gear 5 Awakening", "Toei Animation", "Drums of Liberation sound across Onigashima -> Luffy bursts into cartoon laughter with white hair.", "0.0s / 8.0s", "145", "DRUMS OF LIBERATION")
        ]
    },
    {
        "id": "coldest_antagonist_moments",
        "name": "COLDEST ANTAGONIST MOMENTS",
        "focus": "Infinite Negative Aura & Humiliation of Heroes",
        "title": "Anime Villains With",
        "subject": "INFINITE NEGATIVE AURA",
        "version": "(Coldest Disrespect)",
        "hook_title": "Anime Villains With Literal Negative Aura 🥶💀 #shorts #animevillain #aura #cold",
        "audio_stem": "public/audio/stems/coldest_villains_bed.mp3",
        "audio_source": "DVRST & Ghostface Playa - Negative Aura Anthem",
        "audio_bg_vol": 0.12,
        "story_arc": "Hero launches maximum effort attack -> Antagonist reacts with zero effort or cold gesture -> Protagonist's soul crumbles.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "Naruto Shippuden - Madara Dusts Off Armor", "Studio Pierrot", "Entire Shinobi Alliance hurls jutsu -> Madara brushes speck of dust off his chest.", "0.0s / 4.2s", "50", "ZERO EFFORT"),
            ("4", "Level 2", "Hunter x Hunter - Meruem Passes Netero", "Madhouse", "Meruem walks past the greatest Nen master like he doesn't exist.", "0.0s / 5.0s", "70", "TRANSCENDENT GAP"),
            ("3", "Level 3", "Jujutsu Kaisen S2 - Sukuna 'Stand Proud'", "MAPPA", "Sukuna stands over Jogo in flames: 'Stand proud, you are strong.'", "0.0s / 5.5s", "85", "STAND PROUD"),
            ("2", "Level 4", "Bleach - Aizen Stops Ichigo's Theme Song", "Studio Pierrot", "Aizen stops Ichigo's Bankai blade with a single index finger and stops the background music.", "0.0s / 6.5s", "115", "STOPPED THE OST"),
            ("1", "Level 5", "Monster - Johan Liebert Points To Forehead", "Madhouse", "Johan points to his forehead in burning hospital, smiling at Dr. Tenma.", "0.0s / 8.0s", "140", "TRUE PSYCHOPATHIC AURA")
        ]
    },
    {
        "id": "overpowered_mc_flexes",
        "name": "OVERPOWERED MC FLEXES",
        "focus": "Zero Damage Taken & Instant Traumatizing Counters",
        "title": "When The MC Stops",
        "subject": "HOLDING BACK THEIR POWER",
        "version": "(Absolute Domination)",
        "hook_title": "When The Overpowered MC Stops Holding Back 😈⚡ #shorts #opmc #animeflex",
        "audio_stem": "public/audio/stems/op_mc_bed.mp3",
        "audio_source": "Kute - AVOID ME (Bass Boosted Flex Edit)",
        "audio_bg_vol": 0.13,
        "story_arc": "Enemy boasts and unleashes supreme ultimate spell -> MC stands motionless -> Nonchalant counter wipes enemy existence.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "Overlord - Ainz Ooal Gown 'Grasp Heart'", "Madhouse", "Knight charges in full plate armor -> Ainz casts Grasp Heart -> Knight collapses instantly.", "0.0s / 4.0s", "45", "INSTANT DEATH"),
            ("4", "Level 2", "The Eminence in Shadow - Cid 'I Am Atomic'", "Nexus", "Cid whispers 'I... Am... Atomic' -> Shockwave expands in deep violet light.", "0.0s / 5.0s", "65", "I AM ATOMIC"),
            ("3", "Level 3", "Solo Leveling - Sung Jinwoo 'Arise'", "A-1 Pictures", "Red Knight Igris falls -> Jinwoo commands shadows: 'Arise' -> Blue flames erupt.", "0.0s / 5.5s", "90", "ARISE COMMAND"),
            ("2", "Level 4", "The Misfit of Demon King Academy - Anos Heartbeat", "SILVER LINK.", "Anos kills god of time with his heartbeat: 'Did you think killing me would make me die?'", "0.0s / 6.5s", "115", "HEARTBEAT KILL"),
            ("1", "Level 5", "One Punch Man - Saitama 'Serious Punch'", "Madhouse", "Boros unleashes star-collapsing cannon -> Saitama delivers Serious Punch -> Atmosphere parts.", "0.0s / 8.0s", "140", "SERIOUS SERIES")
        ]
    },
    {
        "id": "mind_game_tactical_battles",
        "name": "200 IQ TACTICAL BATTLES",
        "focus": "Brute Force Meant Nothing (Death Note / Geass)",
        "title": "Anime Battles Where",
        "subject": "BRUTE FORCE MEANT NOTHING",
        "version": "(200 IQ Outplays)",
        "hook_title": "Anime Battles Where Brute Force Meant Nothing 🧠⚡ #shorts #mindgames #anime",
        "audio_stem": "public/audio/stems/mind_games_bed.mp3",
        "audio_source": "Yoshihisa Hirano - Low of Solipsism (Death Note Remaster)",
        "audio_bg_vol": 0.12,
        "story_arc": "Complex psychological web -> Fast analytical deduction cuts -> Inescapable checkmate trap sprung.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "Classroom of the Elite - Ayanokoji Rooftop Trap", "Lerche", "Ryuen thinks he cornered Ayanokoji -> Ayanokoji reveals everyone was just a tool.", "0.0s / 4.5s", "50", "TOOL MONOLOGUE"),
            ("4", "Level 2", "No Game No Life - Sora's Materialization Shiritori", "Madhouse", "Sora removes atmospheric oxygen and nuclear mantle to checkmate Jibril.", "0.0s / 5.0s", "70", "SHIRITORI OUTPLAY"),
            ("3", "Level 3", "Code Geass - Lelouch Zero Requiem Broadcast", "Sunrise", "Schneizel's fleet surrounded as Damocles shield calculation backfires.", "0.0s / 5.5s", "90", "CHECKMATE SCHNEIZEL"),
            ("2", "Level 4", "JoJo: Battle Tendency - Joseph Joestar 'Next You'll Say'", "David Production", "Joseph predicts Esidisi's exact sentence and ties string trap around volcano spikes.", "0.0s / 6.2s", "110", "YOUR NEXT LINE IS"),
            ("1", "Level 5", "Death Note - Light Yagami Potato Chip & Lind L. Tailor", "Madhouse", "L uses Lind L. Tailor television broadcast to pinpoint Kira's exact Kanto district.", "0.0s / 7.5s", "135", "L PINPOINTS KIRA")
        ]
    },
    {
        "id": "saddest_backstories_tearjerkers",
        "name": "SADDEST TEARJERKER MOMENTS",
        "focus": "Emotional Damage & Tragic Pasts",
        "title": "Anime Backstories That",
        "subject": "PERMANENTLY DAMAGE YOU",
        "version": "(Emotional Tears)",
        "hook_title": "Anime Backstories That Will Emotionally Damage You 😭💔 #shorts #sadanime #tearjerker",
        "audio_stem": "public/audio/stems/saddest_moments_bed.mp3",
        "audio_source": "Evan Call - The Voice in My Heart (Violet Evergarden OST)",
        "audio_bg_vol": 0.12,
        "story_arc": "Heartwarming childhood memory -> Cruel reality shatters innocence -> Lifelong emotional trauma revealed.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "One Piece - Chopper and Dr. Hiluluk's Cherry Blossom", "Toei Animation", "Hiluluk drinks poison soup smiling: 'When does a man die? When he is forgotten!'", "0.0s / 4.5s", "50", "HILULUK'S FAREWELL"),
            ("4", "Level 2", "Demon Slayer - Akaza & Koyuki's Past", "ufotable", "Hakuji weeps over poisoned well as Koyuki holds his demon hands in limbo.", "0.0s / 5.2s", "75", "HAKUJI FORGIVEN"),
            ("3", "Level 3", "Assassination Classroom - Koro-sensei's Final Attendance", "Lerche", "Nagisa holds knife trembling over Koro-sensei's heart as roll call finishes.", "0.0s / 5.8s", "95", "FINAL ROLL CALL"),
            ("2", "Level 4", "Naruto Shippuden - Itachi's Final Poke to Sasuke", "Studio Pierrot", "Edo Itachi touches Sasuke's forehead: 'I will love you always.'", "0.0s / 6.5s", "120", "I WILL LOVE YOU ALWAYS"),
            ("1", "Level 5", "Violet Evergarden - Episode 10 Letters to Anne", "Kyoto Animation", "Mother's 50 years of birthday letters delivered to her orphaned daughter across decades.", "0.0s / 8.0s", "145", "50 YEARS OF LETTERS")
        ]
    },
    {
        "id": "insane_plot_twists",
        "name": "INSANE PLOT TWISTS",
        "focus": "Traitor Reveals & Narrative Shockers",
        "title": "Anime Plot Twists That",
        "subject": "LEFT EVERYONE SPEECHLESS",
        "version": "(Total Shock)",
        "hook_title": "Anime Plot Twists That Left The Entire World In Shock 😱🤯 #shorts #plottwist #anime",
        "audio_stem": "public/audio/stems/plot_twists_bed.mp3",
        "audio_source": "Hiroyuki Sawano - APETITAN (Plot Reveal Climax)",
        "audio_bg_vol": 0.13,
        "story_arc": "Casual dialogue or routine event -> Shocking phrase uttered with deadpan casualness -> Sudden earth-shattering reality shift.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "Madoka Magica - Soul Gem Truth Revealed", "Shaft", "Kyubey explains Soul Gems contain actual souls; magical girls become witches.", "0.0s / 4.5s", "50", "INCUBATOR CONTRACT"),
            ("4", "Level 2", "Steins;Gate - Suzuha's 'I Failed' Letter", "White Fox", "Okabe opens blood-stained letter from 1975 repeating 'I failed I failed I failed'.", "0.0s / 5.0s", "70", "I FAILED LETTER"),
            ("3", "Level 3", "Bleach - Aizen Takes Off His Glasses", "Studio Pierrot", "Aizen slicks back his hair on the Sokyoku Hill: 'No one stands in the heavens.'", "0.0s / 5.8s", "90", "AIZEN REVEAL"),
            ("2", "Level 4", "Attack on Titan S4 - Eren Manipulated Grisha", "MAPPA", "Zeke realizes Eren walked Grisha through memories to slaughter the Reiss family.", "0.0s / 6.5s", "115", "EREN DIRECTED IT ALL"),
            ("1", "Level 5", "Attack on Titan S2 - Reiner & Bertholdt Casual Confession", "Wit Studio", "Reiner: 'I'm the Armored Titan, and he's the Colossal Titan.' Lightning flags blow in wind.", "0.0s / 8.0s", "140", "CASUAL CONFESSION")
        ]
    },
    {
        "id": "best_anime_duos_rivalries",
        "name": "LEGENDARY DUOS & RIVALRIES",
        "focus": "Brotherhood & Generational Clashing Wills",
        "title": "Greatest Anime Rivalries",
        "subject": "THAT DEFINED GENERATIONS",
        "version": "(Legendary Duos)",
        "hook_title": "Anime Rivalries That Literally Defined An Entire Generation ⚔️🔥 #shorts #animerivals #duo",
        "audio_stem": "public/audio/stems/duos_rivalries_bed.mp3",
        "audio_source": "Yasuharu Takanashi - Spin and Burst (Naruto Dual Guitars)",
        "audio_bg_vol": 0.14,
        "story_arc": "Clashing ideals -> Mutual respect forged in blood -> Simultaneous ultimate technique collision.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "Jujutsu Kaisen - Yuji & Todo 'Best Friends'", "MAPPA", "Boogie Woogie clap rhythm synchronizes with dual Black Flash strikes.", "0.0s / 4.5s", "55", "BOOGIE WOOGIE BROTHERS"),
            ("4", "Level 2", "Hunter x Hunter - Gon & Killua Friendship", "Madhouse", "Killua runs through trees smiling: 'Gon, you are my light.'", "0.0s / 5.0s", "75", "YOU ARE MY LIGHT"),
            ("3", "Level 3", "Dragon Ball Super: Broly - Goku & Vegeta Galick Kamehameha", "Toei Animation", "Blue Goku and Blue Vegeta unleash joint beam barrage against Broly.", "0.0s / 5.5s", "95", "SAIYAN PRIDE DUAL BEAM"),
            ("2", "Level 4", "One Piece - Zoro & Sanji Wano Back-to-Back", "Toei Animation", "Zoro and Sanji defend Luffy: 'When Luffy becomes King, our job is done.'", "0.0s / 6.5s", "120", "WINGS OF THE PIRATE KING"),
            ("1", "Level 5", "Naruto Shippuden - Naruto vs Sasuke Final Valley Clash", "Studio Pierrot", "Rasengan and Chidori collide in silence; ghostly hands of Jiraiya and Itachi support.", "0.0s / 8.0s", "145", "VALLEY OF THE END")
        ]
    },
    {
        "id": "studio_animation_showcases",
        "name": "STUDIO SHOWCASE (MAPPA VS UFOTABLE)",
        "focus": "Studio Wars: Trademark Aesthetics & Sakuga Styles",
        "title": "Which Studio Rules Anime?",
        "subject": "MAPPA VS UFOTABLE VS WIT",
        "version": "(Studio Showcase)",
        "hook_title": "Which Studio Truly Rules The Anime Industry? 🎨⚔️ #shorts #mappa #ufotable #witstudio",
        "audio_stem": "public/audio/stems/studio_showcase_bed.mp3",
        "audio_source": "Tommee Profitt - In The End (Epic Orchestral Hybrid)",
        "audio_bg_vol": 0.13,
        "story_arc": "Trademark studio lighting / framing -> Iconic action kinematics -> Fandom score comparison.",
        "requires_creator_credit": True,
        "ranks": [
            ("5", "Level 1", "Kyoto Animation - Violet Evergarden Parasol Water Jump", "Kyoto Animation", "Violet steps across water lilies in golden sunlight, peak photographic reflection.", "0.0s / 4.5s", "50", "KYOTO HYPER-REALISM"),
            ("4", "Level 2", "Studio Bones - My Hero Academia All Might vs All For One", "Studio Bones", "United States of Smash corkscrews clouds with pure hand-drawn kinetic ink.", "0.0s / 5.2s", "75", "BONES EMOTIONAL IMPACT"),
            ("3", "Level 3", "Wit Studio - Attack on Titan Levi vs Beast Titan", "Wit Studio", "Arifumi Imai's 3D background tracking through giant forest trees.", "0.0s / 5.8s", "95", "WIT 3D MANEUVER SAKUGA"),
            ("2", "Level 4", "MAPPA - Jujutsu Kaisen S2 Sukuna vs Mahoraga", "MAPPA", "Monochrome destruction and relentless speed in modern Shibuya rubble.", "0.0s / 6.5s", "120", "MAPPA UNFILTERED CHAOS"),
            ("1", "Level 5", "ufotable - Demon Slayer Tengen vs Gyutaro Climax", "ufotable", "Nozomu Abe's volumetric fire and sparks illuminate dark red entertainment district.", "0.0s / 8.0s", "145", "UFOTABLE DIGITAL SAKUGA")
        ]
    },
    {
        "id": "first_season_peak_vs_continuous",
        "name": "SEASON 1 PEAK VS CONTINUAL CLIMB",
        "focus": "Trajectory: One-Season Wonder vs Unstoppable Growth",
        "title": "Anime That Peaked In S1",
        "subject": "VS GOT BETTER EVERY SEASON",
        "version": "(Trajectory)",
        "hook_title": "Anime That Peaked In Season 1 vs Anime That Got Even Better 📈📉 #shorts #animereview #anime",
        "audio_stem": "public/audio/stems/trajectory_bed.mp3",
        "audio_source": "Glue70 - Casin (Upbeat Discussion Groove)",
        "audio_bg_vol": 0.11,
        "story_arc": "Examine Season 1 brilliance -> Track the divergence: creative collapse vs compounding mastery.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "The Promised Neverland (Peaked S1: 8.56 -> S2: 5.37)", "CloverWorks", "Grace Field House escape was genius -> Season 2 skipped goldy pond and made PowerPoint.", "0.0s / 4.5s", "55", "BIGGEST S2 DROP"),
            ("4", "Level 2", "One-Punch Man (Peaked S1: 8.50 -> S2: 7.50)", "Madhouse / J.C. Staff", "Shingo Natsume's dream team animator roster in S1 was never matched in S2.", "0.0s / 5.0s", "70", "ANIMATION STUDIO SHIFT"),
            ("3", "Level 3", "Mob Psycho 100 (Climbed: 8.48 -> 8.80 -> 8.65)", "Studio Bones", "Season 2 Mogami arc and Season 3 finale proved consistent godly quality.", "0.0s / 5.5s", "90", "PERFECT TRILOGY"),
            ("2", "Level 4", "Vinland Saga (Climbed: 8.73 -> 8.80)", "Wit Studio / MAPPA", "Prologue was great revenge -> Farmland arc deepened into a philosophical masterpiece.", "0.0s / 6.5s", "115", "FARMLAND MATURITY"),
            ("1", "Level 5", "Attack on Titan (Climbed: 8.54 -> 8.70 -> 9.05 -> 8.80)", "Wit / MAPPA", "From simple shonen zombie survival into the greatest political mystery epic.", "0.0s / 8.0s", "140", "DEFINITIVE TRAJECTORY")
        ]
    },
    {
        "id": "brutal_dark_psychological",
        "name": "BRUTAL DARK PSYCHOLOGICAL",
        "focus": "Grimdark & High Tension Masterpieces",
        "title": "Dark Anime That Are",
        "subject": "NOT FOR THE FAINT OF HEART",
        "version": "(Psychological Grimdark)",
        "hook_title": "Dark Anime That Are DEFINITELY Not For The Weak 💀🩸 #shorts #darkanime #psychological",
        "audio_stem": "public/audio/stems/dark_psychological_bed.mp3",
        "audio_source": "Susumu Hirasawa - Forces / Kevin Penkin - The Rumble of Scientific Triumph",
        "audio_bg_vol": 0.13,
        "story_arc": "False sense of safety -> Unflinching psychological rupture -> Moral abyss where hope dies.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "Neon Genesis Evangelion - Third Impact", "Gainax", "Shinji screams as Unit-01 hovers above the red LCL ocean of souls.", "0.0s / 4.5s", "50", "PSYCHOLOGICAL BREAKDOWN"),
            ("4", "Level 2", "Re:Zero - Subaru's Rabbit Death", "White Fox", "Snow field in Sanctuary turns red as Great Rabbit devours Subaru alive.", "0.0s / 5.0s", "75", "TRUE TRAUMA LOOP"),
            ("3", "Level 3", "Made in Abyss: Dawn of the Deep Soul", "Kinema Citrus", "Bondrewd reveals elevator cartridge sacrifice mechanism to Riko.", "0.0s / 5.8s", "95", "BONDREWD CARTRIDGES"),
            ("2", "Level 4", "Monster - The Red Rose Mansion Mystery", "Madhouse", "Reading 'The Nameless Monster' picture book inside the secret dark room.", "0.0s / 6.5s", "120", "THE NAMELESS MONSTER"),
            ("1", "Level 5", "Berserk - The Eclipse", "OLM", "The Crimson Behelit cries blood as the God Hand descends upon the Band of the Hawk.", "0.0s / 8.0s", "145", "THE ECLIPSE SACRIFICE")
        ]
    },
    {
        "id": "most_satisfying_beatdowns",
        "name": "MOST SATISFYING BEATDOWNS",
        "focus": "Bully Humbled & Instant Karma",
        "title": "Most Satisfying Moments",
        "subject": "WHEN ARROGANCE GOT HUMBLED",
        "version": "(Instant Regret)",
        "hook_title": "Most Satisfying Anime Moments When Arrogance Got Destroyed 👊💥 #shorts #instantkarma #anime",
        "audio_stem": "public/audio/stems/satisfying_beatdowns_bed.mp3",
        "audio_source": "Shiro Sagisu - Treachery (Hard Trap 808 Remaster)",
        "audio_bg_vol": 0.13,
        "story_arc": "Arrogant villain smirks and taunts helpless victims -> Hero arrives with absolute wrath -> Unforgiving, bone-shattering beatdown.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "My Hero Academia - Deku 1,000,000% vs Muscular", "Studio Bones", "Muscular laughs at Kota -> Deku screams 1,000,000% Delaware Detroit Smash into cliff.", "0.0s / 4.5s", "55", "1,000,000% SMASH"),
            ("4", "Level 2", "Fullmetal Alchemist: Brotherhood - Mustang vs Envy", "Studio Bones", "Mustang snaps fingers relentlessly as Envy screams in agony.", "0.0s / 5.0s", "75", "FLAME ALCHEMY WRATH"),
            ("3", "Level 3", "Jujutsu Kaisen S2 - Yuji & Todo vs Mahito", "MAPPA", "Mahito tries to escape through snow -> Yuji chases him like a wolf hunting a rabbit.", "0.0s / 5.8s", "95", "I AM YOU"),
            ("2", "Level 4", "Attack on Titan - Levi Dismantles Beast Titan", "Wit Studio", "Zeke celebrates artillery barrage -> Levi slices through arm and blade into mouth.", "0.0s / 6.5s", "120", "HUMANITY'S STRONGEST"),
            ("1", "Level 5", "One Piece - Luffy Punches Celestial Dragon", "Toei Animation", "Charloss shoots Hachi -> Luffy walks up stairs in pure black and white -> Punches him into manga frame.", "0.0s / 8.0s", "140", "MANGA PUNCH IMPACT")
        ]
    },
    {
        "id": "legendary_speeches_quotes",
        "name": "LEGENDARY SPEECHES & QUOTES",
        "focus": "Chills & Goosebumps Philosophy Monologues",
        "title": "Anime Speeches That",
        "subject": "GIVE YOU ABSOLUTE CHILLS",
        "version": "(Goosebumps Edition)",
        "hook_title": "Anime Speeches That Give You Literal Goosebumps 🫡🔥 #shorts #animespeech #erwinsmith #quotes",
        "audio_stem": "public/audio/stems/speeches_quotes_bed.mp3",
        "audio_source": "Samuel Kim - Erwin's Charge Epic Orchestral Version",
        "audio_bg_vol": 0.11,
        "story_arc": "Silent despair of army/protagonist -> Unshakable voice rises above fear -> Thundering war cry or philosophical revelation.",
        "requires_creator_credit": False,
        "ranks": [
            ("5", "Level 1", "Naruto Shippuden - Madara Uchiha's Reality Quote", "Studio Pierrot", "'Wake up to reality! Nothing ever goes as planned in this accursed world.'", "0.0s / 4.5s", "50", "WAKE UP TO REALITY"),
            ("4", "Level 2", "Demon Slayer: Mugen Train - Rengoku's Mother Promise", "ufotable", "'Set your heart ablaze. Go beyond your limits.' Flame breathing aura rises.", "0.0s / 5.2s", "75", "SET YOUR HEART ABLAZE"),
            ("3", "Level 3", "Fate/Zero - Rider's King of Heroes Banquet", "ufotable", "Iskandar summons Ionian Hetairoi desert reality marble with a laugh.", "0.0s / 5.8s", "95", "ARMY OF THE KING"),
            ("2", "Level 4", "Naruto Shippuden - Pain's Cycle of Hatred", "Studio Pierrot", "Pain hovers over Konoha: 'Feel pain, contemplate pain, accept pain, know pain.'", "0.0s / 6.5s", "120", "FEEL PAIN SHINRA TENSEI"),
            ("1", "Level 5", "Attack on Titan - Commander Erwin Smith's Final Charge", "Wit Studio", "'My soldiers rage! My soldiers scream! My soldiers FIGHT!' Green flares pierce smoke.", "0.0s / 8.0s", "145", "MY SOLDIERS RAGE")
        ]
    }
]

def generate_markdown(spec):
    sub_id = spec["id"]
    sub_name = spec["name"]
    focus = spec["focus"]
    stem = spec["audio_stem"]
    source = spec["audio_source"]
    vol = spec["audio_bg_vol"]
    arc = spec["story_arc"]
    ranks = spec["ranks"]
    requires_credit = spec.get("requires_creator_credit", False)
    
    credit_header = "YES (Mandatory Creator Attribution)" if requires_credit else "YES (Studio & Official Attribution)"
    
    md = f"""---
sub_category_id: {sub_id}
sub_category_name: {sub_name}
niche: whole_anime
focus: "{focus}"
audio_track: {stem}
audio_source: "{source}"
audio_bg_volume: {vol}
compositor: src/remotion/AnimeShort.tsx
cue_sheet: cue_sheet_{sub_id}.json
---

# Sub-Category Skill: `{sub_id}` ("{sub_name}")

> **MANDATORY FOR AI PIPELINE:** This skill defines the production rules, multi-platform search queries, 5-clip escalation ladder, Remotion compositing, Earshot broadcast audio mastering, and automated description credit formatting for **{sub_name}**.

---

## 1. Core Production Rules
1. **Header & Composition Props (`AnimeShort`):**
   - `titleHeader`: `"{spec['title']}"`
   - `subjectHeader`: `"{spec['subject']}"`
   - `versionTag`: `"{spec['version']}"`
   - `subCategoryId`: `"{sub_id}"`
   - `subCategoryName`: `"{sub_name}"`
   - `globalAudioPath`: `"{stem}"`
2. **Escalating Narrative Arc:**
   - **Arc Formula:** {arc}
   - Each clip strictly escalates from **Rank 5 [Level 1]** to **Rank 1 [Level 5]** (the pinnacle climax).
   - Rank 1 features a mysterious locked badge (`[ 🔒 LOCKED ? ]`) on the left ladder until its reveal.
3. **Audio Architecture (Earshot Standard):**
   - Uses **{source}** mixed at `volume: {vol}` ducked by `-14.0 dB` under character Japanese voice lines and screams.
   - Mastered to YouTube Shorts broadcast standards: **`-14.0 LUFS ± 1.0`**, True Peak `≤ -1.5 dBTP`.
4. **Mandatory Credit Attribution in Description:**
   - Requires Creator / Studio Credit: **{credit_header}**
   - Automatically populates the video description with author handles, source URLs, anime titles, studios, and legal fair-use disclaimers.

---

## 2. Multi-Platform Sourcing Queries

- **YouTube Shorts (`yt-dlp` reverse-engineered search):**
  - `"{spec['subject'].lower()} clips 1080p #shorts"`
  - `"{spec['title'].lower()} {spec['subject'].lower()} anime"`
  - `"best anime {sub_id.replace('_', ' ')} moments 60fps"`
- **TikTok & Instagram Reels (Reverse-Engineered Tags):**
  - `#animeedit #animetrend #{sub_id} #sakuga #animefyp`
- **Reddit JSON API (`/r/AnimeEdits`, `/r/sakuga`, `/r/anime`):**
  - `"site:v.redd.it {sub_id.replace('_', ' ')}"`
- **SakugaBooru REST API (`/post.json`):**
  - `tags=fighting order:score limit=15`

### Universal Negative Filters (Instant Disqualification):
- Low quality (<720p / 480p rips), screen recordings with battery icons, facecam reactions, watermarks covering the center action, and foreign sub clashing.

---

## 3. Verified 5-Clip Benchmark Ladder (Rank 5 -> Rank 1)

| Rank | Level | Anime & Scene | Studio / Creator | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Impact Frame Offset | Kinetic Punchline Text |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
"""
    for r in ranks:
        md += f"| **{r[0]}** | {r[1]} | {r[2]} | {r[3]} | {r[4]} | `{r[5]}` | `{r[6]}` | `{r[7]}` |\n"

    md += f"""
---

## 4. Automated Description & Attribution Template

```text
🏆 {sub_name} — {focus}
Which anime took the #1 spot? Drop your personal ranking in the comments! 👇🔥

══════════════════════════════════════════
🎬 FEATURED CLIPS & CREATOR CREDITS:
══════════════════════════════════════════
[Level 1] Rank 5: {ranks[0][2]} • Credit: {ranks[0][3]}
[Level 2] Rank 4: {ranks[1][2]} • Credit: {ranks[1][3]}
[Level 3] Rank 3: {ranks[2][2]} • Credit: {ranks[2][3]}
[Level 4] Rank 2: {ranks[3][2]} • Credit: {ranks[3][3]}
[Level 5] Rank 1: {ranks[4][2]} • Credit: {ranks[4][3]}

══════════════════════════════════════════
🎵 MUSIC & AUDIO CREDITS:
══════════════════════════════════════════
• Audio Bed: {source}

══════════════════════════════════════════
⚖️ COPYRIGHT & FAIR USE DISCLAIMER:
══════════════════════════════════════════
All footages, audio, edits, and characters used in this video belong to their respective anime studios, animators, and content creators.
This video is a transformative commentary and ranking compilation created under Fair Use guidelines (Section 107 of the Copyright Act 1976).
Full credit is proudly given to the talented creators, editors, and studios credited above.

#shorts #anime #{sub_id} #animerecommendations #sakuga
```

---

## 5. Render, Mastering & Automated QA Commands

1. **Remotion 30 FPS Composition:**
   ```bash
   npx remotion render src/remotion/index.ts AnimeShort output/{sub_id}_raw.mp4 --props=cue_sheet_{sub_id}.json --overwrite
   ```
2. **EBU R128 Loudness Normalization (`-14.0 LUFS`):**
   ```bash
   ffmpeg -y -i output/{sub_id}_raw.mp4 -af "loudnorm=I=-14.0:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/{sub_id}_mastered.mp4
   ```
3. **Frame-by-Frame QA Contact Sheet (Zero Black Frames Guard):**
   ```bash
   ffmpeg -y -i output/{sub_id}_mastered.mp4 -vf "fps=1,scale=260:-1,tile=6x7" -frames:v 1 -q:v 3 output/{sub_id}_qa_sheet.jpg
   ```
"""
    return md

for spec in ALL_20_SPECS:
    file_path = os.path.join(SKILLS_DIR, f"{spec['id']}.md")
    content = generate_markdown(spec)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated skill: {spec['id']}.md")

print(f"\n[Done] Successfully generated all {len(ALL_20_SPECS)} subcategory skills in {SKILLS_DIR}!")
