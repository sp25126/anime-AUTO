#!/usr/bin/env python3
"""
Master Group C Batch Renderer: C8 through C25
Channel: @animefandom0_0
Renders viral uncut dialogue/action moments across Group C subcategories:
16:9 uncropped anime centered over dynamic blurred background + EBU R128 (-14.0 LUFS) audio + 2.0s branded attribution outro card.
Strictly shows the full scene up to 57.5s (+2.0s outro card = <= 59.5s total), staying safely under YouTube Shorts' 60.0s boundary.
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = WORKSPACE_ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

TARGETS_C8_TO_C25 = [
    {
        "id": "c8",
        "key": "moment_underdog_silences_crowd",
        "input": "input/group_a_harvest/full_Black_Clover_sVpubrLKmwU.mp4",
        "output": "output/auto_group_c8_underdog_silences_crowd_master.mp4",
        "creator": "@BlackCloverClips",
        "anime": "Black Clover",
        "hook": "The Entire Stadium Went Dead Silent In 3 Seconds 💀 | Black Clover #shorts #anime",
        "theme": "The Underdog Silences The Entire Crowd"
    },
    {
        "id": "c9",
        "key": "moment_menacing_presence_walk",
        "input": "input/group_a_harvest/full_Solo_Leveling_4rnY9oTtQCM.mp4",
        "output": "output/auto_group_c9_menacing_presence_walk_master.mp4",
        "creator": "@SoloLevelingHub",
        "anime": "Solo Leveling",
        "hook": "Bro's Presence Alone Made Them Drop Their Weapons 🥶 | Solo Leveling #shorts #anime",
        "theme": "The Unstoppable Walking Hazard Presence"
    },
    {
        "id": "c10",
        "key": "moment_instant_technique_copy",
        "input": "input/group_a_harvest/full_Fate_iXtpzE09Ccs.mp4",
        "output": "output/auto_group_c10_instant_technique_copy_master.mp4",
        "creator": "@FateSakuga",
        "anime": "Fate Series",
        "hook": "He Saw It ONCE And Perfected It Instantly ⚡ | Fate Series #shorts #anime",
        "theme": "The Instant Master Technique Copy Flex"
    },
    {
        "id": "c11",
        "key": "moment_heartbreaking_body_shield",
        "input": "input/group_a_harvest/full_Demon_Slayer_GBcj2wT-INA.mp4",
        "output": "output/auto_group_c11_heartbreaking_body_shield_master.mp4",
        "creator": "@DemonSlayerVibes",
        "anime": "Demon Slayer",
        "hook": "His Body Moved On Its Own... 💔😭 | Demon Slayer #shorts #anime",
        "theme": "The Heartbreaking Sacrificial Body Shield"
    },
    {
        "id": "c12",
        "key": "moment_mascot_true_form_reveal",
        "input": "assets/dandadan_raw/clip_1_LQIL6uLsLjw.mp4",
        "output": "output/auto_group_c12_mascot_true_form_reveal_master.mp4",
        "creator": "@DandadanDaily",
        "anime": "Dandadan",
        "hook": "They Thought It Was A Cute Pet Until It Transformed 😱 | Dandadan #shorts #anime",
        "theme": "Harmless Pet Unleashes Colossal True Form"
    },
    {
        "id": "c13",
        "key": "moment_touch_them_and_die",
        "input": "input/group_a_harvest/full_Mob_Psycho_100_sowJm0JQE9A.mp4",
        "output": "output/auto_group_c13_touch_them_and_die_master.mp4",
        "creator": "@MobPsychoEdits",
        "anime": "Mob Psycho 100",
        "hook": "The Single Biggest Mistake In Anime History 💀 | Mob Psycho 100 #shorts #anime",
        "theme": "The 'You Hurt My Loved One' Death Warrant"
    },
    {
        "id": "c14",
        "key": "moment_stare_of_pure_death",
        "input": "input/group_a_harvest/full_Vinland_Saga_Z48sbgGPXk4.mp4",
        "output": "output/auto_group_c14_stare_of_pure_death_master.mp4",
        "creator": "@VinlandSagaHub",
        "anime": "Vinland Saga",
        "hook": "That One Stare Took 10 Years Off His Life 🥶 | Vinland Saga #shorts #anime",
        "theme": "The Stare That Took 10 Years Off His Life"
    },
    {
        "id": "c15",
        "key": "moment_genius_bluff_success",
        "input": "input/group_a_harvest/full_One_Piece_UWTL94XSRO8.mp4",
        "output": "output/auto_group_c15_genius_bluff_success_master.mp4",
        "creator": "@OnePieceShorts",
        "anime": "One Piece",
        "hook": "0% Plan, But 100% Confidence and It WORKED 😂 | One Piece #shorts #anime",
        "theme": "The 0% Plan, 100% Confidence Master Bluff"
    },
    {
        "id": "c16",
        "key": "moment_standing_on_pure_willpower",
        "input": "input/group_a_harvest/full_Berserk_pPPlW_sLoXM.mp4",
        "output": "output/auto_group_c16_standing_on_pure_willpower_master.mp4",
        "creator": "@BerserkLegacy",
        "anime": "Berserk",
        "hook": "Even In Death, He Refused To Fall 👑 | Berserk #shorts #anime",
        "theme": "The Undefeated Stand on Pure Willpower"
    },
    {
        "id": "c17",
        "key": "moment_holding_back_percentage_reveal",
        "input": "input/group_a_harvest/full_Frieren_Fc7VSKl1Dyo.mp4",
        "output": "output/auto_group_c17_holding_back_percentage_reveal_master.mp4",
        "creator": "@FrierenClips",
        "anime": "Frieren: Beyond Journey's End",
        "hook": "He Thought They Were Equal Until Bro Dropped This Line 🥶 | Frieren #shorts #anime",
        "theme": "The 'That Was Only 10% Power' Reality Drop"
    },
    {
        "id": "c18",
        "key": "moment_cold_blood_revenge_execution",
        "input": "input/group_a_harvest/full_Tokyo_Ghoul_o8pkvlJ9lQE.mp4",
        "output": "output/auto_group_c18_cold_blood_revenge_execution_master.mp4",
        "creator": "@TokyoGhoulZone",
        "anime": "Tokyo Ghoul",
        "hook": "Bro Did Not Let Him Finish His Villain Monologue 💀 | Tokyo Ghoul #shorts #anime",
        "theme": "The Cold-Blooded No-Mercy Revenge Execution"
    },
    {
        "id": "c19",
        "key": "moment_weapon_awakening_release",
        "input": "input/group_a_harvest/full_Bleach_TdFxPWkbktI.mp4",
        "output": "output/auto_group_c19_weapon_awakening_release_master.mp4",
        "creator": "@BleachSakuga",
        "anime": "Bleach TYBW",
        "hook": "The Sky Changed Color When He Unsheathed This Blade ⚔️ | Bleach #shorts #anime",
        "theme": "First Legendary Weapon / Shikai Unsheathing"
    },
    {
        "id": "c20",
        "key": "moment_unspoken_mutual_respect",
        "input": "input/group_a_harvest/full_Jujutsu_Kaisen_BbuvqdCoWPA.mp4",
        "output": "output/auto_group_c20_unspoken_mutual_respect_master.mp4",
        "creator": "@JJKMoments",
        "anime": "Jujutsu Kaisen",
        "hook": "When Two Monsters Acknowledge Each Other Without A Word 🤝 | Jujutsu Kaisen #shorts",
        "theme": "The Unspoken Nod of Two Peak Monsters"
    },
    {
        "id": "c21",
        "key": "moment_cold_indifference_walkaway",
        "input": "input/group_a_harvest/full_Fire_Force_QRRkPhv_P34.mp4",
        "output": "output/auto_group_c21_cold_indifference_walkaway_master.mp4",
        "creator": "@FireForceOfficial",
        "anime": "Fire Force",
        "hook": "Bro Walked Away Before The Attack Even Landed 💀 | Fire Force #shorts #anime",
        "theme": "Cold Indifference Walkaway / Utter Disregard"
    },
    {
        "id": "c22",
        "key": "moment_villain_apologizes_in_terror",
        "input": "input/group_a_harvest/full_Solo_Leveling_qrrd85ToLCI.mp4",
        "output": "output/auto_group_c22_villain_apologizes_in_terror_master.mp4",
        "creator": "@SoloLevelingAura",
        "anime": "Solo Leveling",
        "hook": "The Exact Second The Villain Realized He Was Cooked 😭 | Solo Leveling #shorts #anime",
        "theme": "Arrogant Villain Apologizes In Pure Terror"
    },
    {
        "id": "c23",
        "key": "moment_one_finger_block_shock",
        "input": "input/group_a_harvest/full_Fate_-hIEMOGO3Go.mp4",
        "output": "output/auto_group_c23_one_finger_block_shock_master.mp4",
        "creator": "@FateAnimeHub",
        "anime": "Fate Series",
        "hook": "He Stopped Their Strongest Attack With ONE FINGER 😱 | Fate Series #shorts #anime",
        "theme": "The Effortless One-Finger Block Humiliation"
    },
    {
        "id": "c24",
        "key": "moment_battle_iq_counter_trap",
        "input": "input/group_a_harvest/full_Naruto_yn0mnRiqHDg.mp4",
        "output": "output/auto_group_c24_battle_iq_counter_trap_master.mp4",
        "creator": "@NarutoShippudenHub",
        "anime": "Naruto Shippuden",
        "hook": "Bro Calculated This 50 Moves Ahead 🧠⚡ | Naruto Shippuden #shorts #anime",
        "theme": "The 200 IQ Reverse Counter Trap"
    },
    {
        "id": "c25",
        "key": "moment_unhinged_english_dub_masterpiece",
        "input": "assets/dandadan_raw/clip_4_89g7o-KsxFU.mp4",
        "output": "output/auto_group_c25_unhinged_english_dub_masterpiece_master.mp4",
        "creator": "@AnimeDubClips",
        "anime": "Dandadan",
        "hook": "The English Dub Voice Actors Had ZERO Chill Here 😭💀 | Dandadan #shorts #anime",
        "theme": "Unhinged / Out-of-Pocket English Dub Delivery"
    }
]

def render_group_c_short(input_clip: str, output_path: str, creator_tag: str, anime_name: str, max_dur: float = 57.5) -> str:
    print(f"\n[Group C Renderer] Processing: {Path(input_clip).name} -> {Path(output_path).name}")
    probe_cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', str(input_clip)]
    d = json.loads(subprocess.check_output(probe_cmd).decode('utf-8'))
    tot = float(d['format']['duration'])
    
    # Show the full scene as much as possible, leaving 2.0s for the branded outro card
    trim_dur = min(tot, max_dur)
    print(f"  Raw Duration: {tot:.2f}s | Full Scene Preserved: {trim_dur:.2f}s (+ 2.0s outro card = {trim_dur+2.0:.2f}s)")
    
    # 1. 16:9 uncropped over dynamic blurred background + EBU R128 audio (-14.0 LUFS, -1.5 TP)
    temp_base = output_path.replace('.mp4', '_base.mp4')
    cmd = [
        'ffmpeg', '-y', '-ss', '0', '-t', str(trim_dur), '-i', str(input_clip),
        '-filter_complex',
        '[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,eq=brightness=-0.15:contrast=1.05[bg];'
        '[0:v]scale=1080:-1[fg];'
        '[bg][fg]overlay=0:(1920-h)/2[v];'
        '[0:a]aresample=48000,loudnorm=I=-14.0:TP=-1.5:LRA=11[a]',
        '-map', '[v]', '-map', '[a]',
        '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
        '-c:a', 'aac', '-b:a', '192k',
        temp_base
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # 2. 2-second Pillow Outro Attribution Card
    outro_png = output_path.replace('.mp4', '_outro.png')
    img = Image.new('RGBA', (1080, 1920), (10, 12, 16, 255))
    draw = ImageDraw.Draw(img)
    font_brand = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 52)
    font_label = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 46)
    font_tag = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 64)
    
    bw = draw.textbbox((0,0), '@animefandom0_0', font=font_brand)[2]
    draw.text(((1080-bw)//2, 820), '@animefandom0_0', font=font_brand, fill=(255,255,255,255))
    
    lw = draw.textbbox((0,0), 'ORIGINAL CLIP BY', font=font_label)[2]
    draw.text(((1080-lw)//2, 910), 'ORIGINAL CLIP BY', font=font_label, fill=(255,230,0,255))
    
    cw = draw.textbbox((0,0), creator_tag, font=font_tag)[2]
    for dx, dy in [(-3,0),(3,0),(0,-3),(0,3)]:
        draw.text(((1080-cw)//2+dx, 980+dy), creator_tag, font=font_tag, fill=(0,0,0,255))
    draw.text(((1080-cw)//2, 980), creator_tag, font=font_tag, fill=(255,255,255,255))
    img.save(outro_png)
    
    temp_outro = output_path.replace('.mp4', '_outro.mp4')
    cmd_o = [
        'ffmpeg', '-y', '-loop', '1', '-i', outro_png,
        '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=48000',
        '-t', '2.0', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
        '-c:a', 'aac', '-b:a', '192k', '-r', '30', temp_outro
    ]
    subprocess.run(cmd_o, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # 3. Concatenate base + outro
    concat_txt = output_path.replace('.mp4', '_concat.txt')
    with open(concat_txt, 'w', encoding='utf-8') as f:
        f.write(f"file '{os.path.abspath(temp_base)}'\nfile '{os.path.abspath(temp_outro)}'\n")
    
    cmd_stitch = [
        'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', concat_txt,
        '-c', 'copy', output_path
    ]
    subprocess.run(cmd_stitch, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # Cleanup temporary files
    for tmp in [temp_base, outro_png, temp_outro, concat_txt]:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass
                
    print(f"  ✅ Render complete: {output_path}")
    return output_path

def main():
    print("=" * 70)
    print("🎬 MASTER PRODUCTION: RENDERING GROUP C (C8 THROUGH C25)")
    print("=" * 70)
    t0 = time.time()
    success = []
    failed = []
    
    for t in TARGETS_C8_TO_C25:
        cid = t["id"].upper()
        inp = os.path.join(WORKSPACE_ROOT, t["input"])
        out = os.path.join(WORKSPACE_ROOT, t["output"])
        
        if not os.path.exists(inp):
            print(f"❌ Input not found for {cid}: {inp}")
            failed.append((cid, "Input missing"))
            continue
            
        try:
            render_group_c_short(
                input_clip=inp,
                output_path=out,
                creator_tag=t["creator"],
                anime_name=t["anime"],
                max_dur=57.5
            )
            success.append((cid, out))
        except Exception as e:
            print(f"❌ Render failed for {cid}: {e}")
            failed.append((cid, str(e)))
            
    print("\n" + "=" * 70)
    print(f"🎉 BATCH RENDER COMPLETE in {time.time()-t0:.1f}s")
    print(f"✅ Successfully rendered: {len(success)}/18")
    if failed:
        print(f"❌ Failed: {len(failed)}/18: {failed}")
    print("=" * 70)

if __name__ == "__main__":
    main()
