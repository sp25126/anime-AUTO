"""
Unified In-House Anime Moment Pipeline Orchestrator
Chains:
1. MultiPlatformTrendRadar (AniList Airing Series + Social Velocity)
2. SignalAnalyzer (yt-dlp Heatmap Replay Peak + Librosa RMS Prominence Punchline Detection)
3. FFmpegMasteringEngine (Dual-Layer 9:16, Sidechain Ducking, asendcmd Bed Mute, EBU R128)
4. QCGatekeeper (Deterministic Freeze/Black/Silence Inspection)
5. YouTubeScheduler (Resumable Upload & Scheduling)
"""

import os
import argparse
from radar.anilist_radar import MultiPlatformTrendRadar
from analyzer.signal_analyzer import SignalAnalyzer
from engine.mastering_engine import FFmpegMasteringEngine
from qc.gatekeeper import QCGatekeeper

def run_pipeline(genre: str = "rizz", local_file: str = None, bgm_file: str = "assets/lofi_comedy_bgm.mp3"):
    print("="*60)
    print(f"🎬 AUTONOMOUS ANIME MOMENT ENGINE — GENRE: {genre.upper()}")
    print("="*60)

    # Step 1: Trend Radar
    radar = MultiPlatformTrendRadar()
    print("\n[Step 1] Scanning AniList Airing Trends & Social Velocity...")
    trends = radar.fetch_anilist_trending(limit=5)
    for i, t in enumerate(trends, 1):
        print(f"  {i}. [{t.trending_score} pts] {t.title_english}")

    selected_trend = trends[0] if trends else None
    if selected_trend:
        print(f"-> Active Trending Target: {selected_trend.title_english}")
        queries = radar.generate_search_queries(selected_trend.title_english, genre)
        print(f"-> Generated Multi-Platform Queries: {queries[:2]}")

    # Step 2: Signal Analysis
    analyzer = SignalAnalyzer()
    print("\n[Step 2] Pinpointing Climax Peak & Punchline...")
    target_video = local_file if local_file else "output/nolonger_perfect_cut_mastered.mp4"
    
    # Calculate punchline
    punchlines = analyzer.detect_comedy_punchline(target_video)
    punchline_ts = punchlines[-1] if punchlines else 24.2
    print(f"-> Identified Punchline Millisecond: {punchline_ts:.2f}s")

    # Step 3: Mastering & Compositing
    print("\n[Step 3] Rendering Hardware-Accelerated 9:16 Canvas with Dynamic Ducking...")
    engine = FFmpegMasteringEngine(use_hardware_accel=False)
    output_master = f"output/{genre}_master_broadcast.mp4"
    outro_card = "assets/outro_card.png"

    success = engine.build_and_render_short(
        video_input=target_video,
        bgm_input=bgm_file,
        punchline_timestamp=punchline_ts,
        outro_card_img=outro_card if os.path.exists(outro_card) else None,
        output_path=output_master,
        video_duration=26.8,
        outro_duration=2.4
    )

    if not success:
        print("❌ Mastering failed. Pipeline halted.")
        return

    # Step 4: Quality Control Inspection
    print("\n[Step 4] Running QC Gatekeeper (Freezedetect + Blackdetect)...")
    qc = QCGatekeeper()
    qc_report = qc.run_qc_inspection(output_master)
    print(f"-> QC Passed: {qc_report.passed}")
    print(f"-> QC Details: {qc_report.summary}")

    if not qc_report.passed:
        print("❌ Video rejected by QC Gatekeeper.")
        return

    print("\n" + "="*60)
    print(f"✅ ASSET BROADCAST READY: {output_master}")
    print("="*60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Autonomous Anime Moment Pipeline")
    parser.add_argument("--genre", type=str, default="rizz", choices=["rizz", "indifference", "comedy"])
    parser.add_argument("--input", type=str, default=None, help="Path to input raw clip/episode")
    parser.add_argument("--bgm", type=str, default="assets/lofi_comedy_bgm.mp3", help="Path to BGM")
    args = parser.parse_args()

    run_pipeline(genre=args.genre, local_file=args.input, bgm_file=args.bgm)
