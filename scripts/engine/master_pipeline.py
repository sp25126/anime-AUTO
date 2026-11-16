"""
Master Autonomous Production Pipeline (AFA-SE Orchestrator)
Orchestrates the entire end-to-end pipeline:
1. Decision Engine (Multi-Horizon Evaluation for Group A or Group C)
2. Stream Harvester (Direct HLS / Micro-clipping)
3. Forensic DSP Engine (Two-pass loudnorm, sidechain ducking, zoompan)
4. QA Gatekeeper & YouTube Scheduler
"""

import sys
import os
import datetime
from decision_engine import MultiHorizonDecisionEngine, AnimeCandidate
from stream_harvester import StreamHarvester
from dsp_engine import ForensicDSPEngine
from qa_scheduler import QAGatekeeper, YouTubeScheduler

def run_pipeline(target_group: str = "C", target_date_utc: datetime.datetime = None):
    print(f"\n=======================================================")
    print(f"🎬 LAUNCHING AUTONOMOUS PRODUCTION FOR GROUP {target_group}")
    print(f"=======================================================\n")
    
    # 1. Decision Engine
    print("[Step 1] Running Multi-Horizon Decision Matrix...")
    engine = MultiHorizonDecisionEngine()
    
    # Example candidate evaluation based on live market signals
    candidates = [
        AnimeCandidate(
            media_id=1,
            title="The Apothecary Diaries",
            v_24_spike=0.88,
            k_7_velocity=0.82,
            e_30_volume=0.95,
            saturation_score=0.10,
            audio_variance=0.92,
            sub_density=0.85,
            genres=["Comedy", "Drama", "Mystery"],
            sample_query="The Apothecary Diaries Jinshi Maomao funny scene eng sub"
        ),
        AnimeCandidate(
            media_id=2,
            title="Hello, I am a Witch and my Crush Wants me to Make a Love Potion!",
            v_24_spike=0.95,
            k_7_velocity=0.75,
            e_30_volume=0.60,
            saturation_score=0.05,
            audio_variance=0.88,
            sub_density=0.90,
            genres=["Fantasy", "Romance"],
            sample_query="Hello, I am a Witch and my Crush Wants me to Make a Love Potion! accidental rizz"
        )
    ]
    
    winner = engine.evaluate_pipeline(candidates, target_group=target_group)
    print(f"🏆 Selected Winning Anime: {winner.title}")
    
    # 2. Harvester
    print(f"\n[Step 2] Sourcing pristine 1080p clip via Harvester...")
    harvester = StreamHarvester()
    raw_clip_path = "input/harvested_winner_clip.mp4"
    # Execute direct micro-clip cut
    harvester.fast_harvest_direct(winner.sample_query, start_time=10.0, duration=15.0, output_path=raw_clip_path)
    
    # 3. Forensic DSP
    print(f"\n[Step 3] Rendering Master with Forensic Audio & Layout...")
    dsp = ForensicDSPEngine(use_gpu=True)
    out_master = f"output/{winner.title.lower().replace(' ', '_')[:20]}_master.mp4"
    rendered = dsp.render_group_c_short(
        clip_path=raw_clip_path,
        bg_path="assets/backgrounds/romcom_sunset.webp",
        header_path="assets/brand_header_card.png",
        bgm_path="output/lofi_rizz_bgm.wav",
        output_path=out_master,
        mute_timestamps=(8.0, 9.5)
    )
    
    # 4. QA Gatekeeper
    if rendered:
        print(f"\n[Step 4] Executing QA Gatekeeper Verification...")
        qa = QAGatekeeper()
        passed = qa.verify_render(out_master)
        if passed:
            print(f"\n✅ PRODUCTION READY FOR YOUTUBE RELEASE: {out_master}")
        else:
            print("\n❌ QA Check Failed! Pipeline aborted.")

if __name__ == "__main__":
    group = sys.argv[1].upper() if len(sys.argv) > 1 else "C"
    run_pipeline(target_group=group)
