"""
Generates dedicated single-anime edits skills in subcategory_skills/
ensuring 100% adherence to the user's rule:
"ranking edits which are only of one anime (e.g. JJK only, Demon Slayer only, AOT only)"
"""

import os
import sys

WORKSPACE = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, WORKSPACE)
from scripts.generate_anime_skills import generate_markdown
SKILLS_DIR = os.path.join(WORKSPACE, "subcategory_skills")

SINGLE_ANIME_SPECS = [
    {
        "id": "jjk_viral_edits",
        "name": "JUJUTSU KAISEN VIRAL EDITS",
        "focus": "Strictly Jujutsu Kaisen Edits Only (Gojo, Sukuna, Toji, Yuta)",
        "title": "Ranking The Best",
        "subject": "JUJUTSU KAISEN EDITS",
        "version": "(JJK Edition)",
        "hook_title": "Ranking The Best Jujutsu Kaisen Edits Of All Time 🔥⚡ #shorts #jjk #jujutsukaisen #animeedit",
        "audio_stem": "public/audio/stems/jjk_edits_bed.mp3",
        "audio_source": "MC GW - Montagem Rugada (JJK Phonk Remix)",
        "audio_bg_vol": 0.12,
        "story_arc": "JJK character aura buildup -> Twixtor speed blitz -> Domain Expansion / cursed energy impact drop.",
        "requires_creator_credit": True,
        "ranks": [
            ("5", "Level 1", "Nanami Kento - 7:3 Ratio Strike Overtime", "@nanamivfx (TikTok)", "Nanami loosens tie and checks watch -> Overtime aura erupts -> Ratio strike crushes wall.", "0.0s / 4.5s", "50", "OVERTIME RATIO STRIKE"),
            ("4", "Level 2", "Yuta Okkotsu - True Love Rika Summon", "@yuta_edits (YouTube)", "Yuta slips on wedding ring -> Black tendrils manifest -> Rika laser beam tears sky.", "0.0s / 5.0s", "70", "PURE UNCONDITIONAL LOVE"),
            ("3", "Level 3", "Toji Fushiguro - Inventory Curse Speed Blitz", "@zenin_flow (Instagram)", "Toji pulls Playful Cloud from worm curse -> Vaults off building -> Sonic velocity dash.", "0.5s / 5.5s", "90", "HEAVENLY RESTRICTION"),
            ("2", "Level 4", "Ryomen Sukuna - Malevolent Shrine Finger Snap", "@sukuna_curse (TikTok)", "Sukuna makes Enmaten hand sign -> Domain cuts slice city blocks in monochrome ribbons.", "0.0s / 6.5s", "115", "MALEVOLENT SHRINE"),
            ("1", "Level 5", "Satoru Gojo - Hollow Purple 'Throughout Heaven'", "@sixeyes_ae (YouTube)", "Gojo pulls down blindfold -> Red and Blue collide -> Infinite Void Hollow Purple blast.", "0.0s / 8.0s", "140", "THROUGHOUT HEAVEN AND EARTH")
        ]
    },
    {
        "id": "demon_slayer_viral_edits",
        "name": "DEMON SLAYER VIRAL EDITS",
        "focus": "Strictly Demon Slayer Edits Only (Tengen, Kokushibo, Akaza, Muichiro)",
        "title": "Ranking The Best",
        "subject": "DEMON SLAYER EDITS",
        "version": "(Kimetsu Edition)",
        "hook_title": "Ranking The Cleanest Demon Slayer Edits 🔥⚔️ #shorts #demonslayer #kimetsunoyaiba #animeedit",
        "audio_stem": "public/audio/stems/demon_slayer_edits_bed.mp3",
        "audio_source": "Ghostface Playa - Why Not (Demon Slayer Breathing Phonk)",
        "audio_bg_vol": 0.12,
        "story_arc": "Breathing form kata initialization -> Smear blade ignition -> Blood demon art counter clash.",
        "requires_creator_credit": True,
        "ranks": [
            ("5", "Level 1", "Muichiro Tokito - Mist Breathing 7th Form Obscuring Clouds", "@mistvfx (TikTok)", "Muichiro vanishes into thick white fog -> Appears behind Gyokko with clean neck decapitation.", "0.0s / 4.5s", "50", "OBSCURING CLOUDS"),
            ("4", "Level 2", "Akaza - Destructive Death Compass Needle Drop", "@akaza_flow (YouTube)", "Akaza stamps foot onto snow -> Snowflake compass flares neon blue -> Hundred chaotic strikes.", "0.0s / 5.0s", "70", "COMPASS NEEDLE"),
            ("3", "Level 3", "Kokushibo - Moon Breathing Crescent Moon Blades", "@upper1_edits (Instagram)", "Kokushibo draws flesh katana -> Chaotic miniature crescent moon blades orbit blade swing.", "0.0s / 5.8s", "95", "MOON BREATHING"),
            ("2", "Level 4", "Rengoku Kyojuro - 9th Form Rengoku Dragon Charge", "@flamehashira (TikTok)", "Rengoku plants stance roaring -> Flame dragon manifests around blade in blistering charge.", "0.0s / 6.5s", "120", "SET YOUR HEART ABLAZE"),
            ("1", "Level 5", "Tengen Uzui - Musical Score Technique Sparks Climax", "@soundhashira (YouTube)", "Tengen blocks poisoned sickles with one hand -> Explosive musical notes detonate in red fireworks.", "0.0s / 8.0s", "145", "MUSICAL SCORE COMPLETE")
        ]
    },
    {
        "id": "aot_viral_edits",
        "name": "ATTACK ON TITAN VIRAL EDITS",
        "focus": "Strictly Attack on Titan Edits Only (Eren, Levi, Erwin, Reiner)",
        "title": "Ranking The Best",
        "subject": "ATTACK ON TITAN EDITS",
        "version": "(Shingeki Edition)",
        "hook_title": "Ranking The Coldest Attack On Titan Edits ⚡💀 #shorts #aot #attackontitan #animeedit",
        "audio_stem": "public/audio/stems/aot_edits_bed.mp3",
        "audio_source": "Hiroyuki Sawano - Ashes on The Fire (Dark Phonk Edit)",
        "audio_bg_vol": 0.13,
        "story_arc": "ODM wire acceleration or titan flesh spark -> Camera swoops in 3D perspective -> Earth-shattering transformation impact.",
        "requires_creator_credit": True,
        "ranks": [
            ("5", "Level 1", "Reiner Braun - Armored Titan Wall Breach Charge", "@reiner_ae (TikTok)", "Armored Titan accelerates through cannon fire -> Slams into Wall Maria gate with explosive shockwave.", "0.0s / 4.5s", "50", "ARMORED IMPACT"),
            ("4", "Level 2", "Erwin Smith - Beast Titan Suicide Charge Monologue", "@erwin_flow (YouTube)", "Erwin leads cavalry into boulder barrage -> Green smoke flare shoots into sky.", "0.0s / 5.2s", "75", "MY SOLDIERS RAGE"),
            ("3", "Level 3", "Levi Ackerman - Kenny Squad ODM Bar Escape", "@ackerman_vfx (Instagram)", "Levi spins through tavern window, hooks ceiling beam, and fires shotgun in mid-air barrel roll.", "0.0s / 5.8s", "95", "KENNY CHASE SAKUGA"),
            ("2", "Level 4", "Levi Ackerman - Beast Titan Forest Dismantle S3", "@humanity_strongest (TikTok)", "Levi corkscrews down Beast Titan arm like a blender -> Slices nape in red spray.", "0.0s / 6.5s", "120", "BEAST TITAN HUMBLED"),
            ("1", "Level 5", "Eren Yeager - Liberio Declaration of War Transformation", "@yeagerist_ae (YouTube)", "Willy Tybur declares war -> Green eyes glow in darkness -> Attack Titan erupts beneath stage.", "0.0s / 8.0s", "145", "DECLARATION OF WAR")
        ]
    },
    {
        "id": "one_piece_viral_edits",
        "name": "ONE PIECE VIRAL EDITS",
        "focus": "Strictly One Piece Edits Only (Gear 5, Zoro, Shanks, Luffy)",
        "title": "Ranking The Best",
        "subject": "ONE PIECE EDITS",
        "version": "(Straw Hat Edition)",
        "hook_title": "Ranking The Greatest One Piece Edits Ever Made 🏴‍☠️🔥 #shorts #onepiece #gear5 #animeedit",
        "audio_stem": "public/audio/stems/one_piece_edits_bed.mp3",
        "audio_source": "Kohei Tanaka - Overtaken (Drums of Liberation Phonk)",
        "audio_bg_vol": 0.14,
        "story_arc": "Conqueror aura crackle -> Cartoon bounce or sword unsheath -> Massive conquerors haki lightning blast.",
        "requires_creator_credit": True,
        "ranks": [
            ("5", "Level 1", "Sanji - Ifrit Jambe Beef Burst", "@vinsmoke_vfx (TikTok)", "Sanji awakens exoskeleton -> Blue flames ignite legs -> Flurry of kicks blasts Queen through Onigashima roof.", "0.0s / 4.5s", "50", "IFRIT JAMBE"),
            ("4", "Level 2", "Shanks - Divine Departure (Kamusari) Blast", "@redhair_ae (YouTube)", "Shanks draws Gryphon -> Red black conquerors lightning arcs -> Kamusari cuts Kid ship in half.", "0.0s / 5.0s", "70", "DIVINE DEPARTURE"),
            ("3", "Level 3", "Roronoa Zoro - King of Hell Three Sword Style vs King", "@zoro_flow (Instagram)", "Zoro lets Enma drain his life force -> Green flame conqueror blades clash with Imperial Dragon.", "0.0s / 5.8s", "95", "KING OF HELL ENMA"),
            ("2", "Level 4", "Luffy - Red Roc Punch Against Kaido in Rooftop Fire", "@strawhat_edits (TikTok)", "Luffy activates Gear 3 -> Flame engulfs giant fist -> Kaido face slammed into stone floor.", "0.0s / 6.5s", "120", "RED ROC IMPACT"),
            ("1", "Level 5", "Luffy - Gear 5 Drums of Liberation Laughing Jump", "@joyboy_vfx (YouTube)", "Luffy bounces against the full moon laughing -> Grabs lightning bolt from thunderclouds.", "0.0s / 8.0s", "145", "WARRIOR OF LIBERATION")
        ]
    },
    {
        "id": "bleach_viral_edits",
        "name": "BLEACH TYBW VIRAL EDITS",
        "focus": "Strictly Bleach & TYBW Edits Only (Ichigo, Aizen, Yamamoto, Yhwach)",
        "title": "Ranking The Best",
        "subject": "BLEACH TYBW EDITS",
        "version": "(Bankai Edition)",
        "hook_title": "Ranking The Coldest Bleach TYBW Edits 🗡️⚡ #shorts #bleach #tybw #animeedit",
        "audio_stem": "public/audio/stems/bleach_edits_bed.mp3",
        "audio_source": "Shiro Sagisu - Number One (Bankai Phonk Remix)",
        "audio_bg_vol": 0.13,
        "story_arc": "Spiritual pressure Reiatsu release -> Whispered Bankai phrase -> Total screen flash / color inversion.",
        "requires_creator_credit": True,
        "ranks": [
            ("5", "Level 1", "Zaraki Kenpachi - Shikai Nozarashi Giant Meteor Slash", "@zaraki_ae (TikTok)", "Kenpachi removes eyepatch -> Giant cleaver Nozarashi swings -> Slices Gremmy meteor clean in half.", "0.0s / 4.5s", "50", "DRINK NOZARASHI"),
            ("4", "Level 2", "Sosuke Aizen - Chair Aizen Black Coffin (Hado 90)", "@aizen_negative_aura (YouTube)", "Aizen bound to chair chants Hado 90 -> Black box gravitational singularity crushes eyeball monsters.", "0.0s / 5.0s", "70", "CHAIR AIZEN HADO 90"),
            ("3", "Level 3", "Genryusai Yamamoto - Bankai Zanka no Tachi South", "@yamamoto_bankai (Instagram)", "Yamamoto drives sword into scorched ground -> 10 trillion dead skeletons emerge from ashes.", "0.0s / 5.8s", "95", "ZANKA NO TACHI SOUTH"),
            ("2", "Level 4", "Ichigo Kurosaki - Horn of Salvation Getsuga Gran Rey Cero", "@kurosaki_flow (TikTok)", "Ichigo manifests single horn -> Merges Hollow Cero with Quincy Getsuga in gold cross blast.", "0.0s / 6.5s", "120", "GRAN REY JUJISHO"),
            ("1", "Level 5", "Sosuke Aizen - Kyoka Suigetsu vs Yhwach Reality Illusion", "@god_aizen (YouTube)", "Yhwach thinks he stabbed Ichigo -> Illusion shatters -> Aizen smirks: 'So you think you are looking at Kurosaki?'", "0.0s / 8.0s", "145", "COMPLETE HYPNOSIS")
        ]
    }
]

if __name__ == "__main__":
    for spec in SINGLE_ANIME_SPECS:
        path = os.path.join(SKILLS_DIR, f"{spec['id']}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(generate_markdown(spec))
        print(f"Generated single-anime skill: {path}")
    print("\n[Done] All single-anime edit skills generated successfully!")
