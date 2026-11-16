# Autonomous Channel Production Architecture (Zero-Touch Specification)
**Channel:** [@animefandom0_0](https://www.youtube.com/@animefandom0_0)  
**Standard:** 100% Autonomous, Zero-Human-Touch Daily Publishing Engine  
**Publishing Window:** Every day at **7:30 PM IST (14:00 UTC)**  

---

## 1. 3-Group Harmonized Publishing Rotation

To maximize YouTube Shorts algorithmic reach, prevent audience fatigue, and trigger different viewer behaviors (comments vs. replays vs. shares), the channel cycles through **3 complementary content archetypes**:

```mermaid
flowchart LR
    A["Day 1: Group A<br/>(Edit Ranking / Sakuga Compilations)"] --> C1["Day 2: Group C<br/>(Micro-Moments / Accidental Rizz)"]
    C1 --> B["Day 3: Group B<br/>(Rotate-Phone Cinematic AMVs)"]
    B --> C2["Day 4: Group C<br/>(Deadpan Reality Checks)"]
    C2 --> A
```

| Group | Content Archetype | Format & Staging | Audio Standard | Algorithmic Driver |
| :--- | :--- | :--- | :--- | :--- |
| **Group A** | **Single-Franchise Viral Rankings** (Top 5 Coldest Auras, Climax Sakuga) | 1080×1920 (9:16), dynamic blur / 4K native, countdown HUD | Phonk / High-octane battle beat drops, bass risers | **High Comment Friction & Shares** (*"Who had #1?"*) |
| **Group B** | **Rotate-Phone Cinematic AMV** (0° to -90° IMAX Action) | Animated phone-tilt hook (0–2s), counter-clockwise rotation into fullscreen landscape | Spatial foley, massive sub-bass drops, zero intrusive SFX | **High Watch-Time & Interaction** (*Viewer tilts device*) |
| **Group C** | **Micro-Moments & Accidental Rizz** (Jinshi, Dandadan, Frieren) | 1080×608 uncropped 16:9 at `y=656`, flush header at `y=456`, parallax wallpaper | Warm lofi bed, -15 dB sidechain ducking, deadpan mute | **High APV (>95%) & Second Loops** (*Relatable comedy*) |

---

## 2. The 5-Stage Zero-Touch Pipeline

Every day at **02:00 UTC (7:30 AM IST)**, the automated daemon wakes up and executes the following sequence:

```mermaid
sequenceDiagram
    autonumber
    participant D as Multi-Horizon Decision Engine
    participant H as Reverse Stream Harvester
    participant DSP as Forensic DSP Engine
    participant QA as Gatekeeper QA
    participant YT as YouTube Data API v3

    D->>D: 1. Ingest Daily (AniList), Weekly (Karma), Monthly (Evergreen)
    D->>D: 2. Calculate S_A, S_B, or S_C score & check pHash saturation
    D->>H: 3. Dispatch winning anime & timecodes
    H->>H: 4. JA4 TLS WAF Bypass & remote HLS stream seek (-c copy)
    H->>DSP: 5. Hand over raw 1080p clip
    DSP->>DSP: 6. Pass 1 Loudness Analysis + Pass 2 Render (sidechain ducking, -14 LUFS)
    DSP->>QA: 7. Hand over final_rendered_short.mp4
    QA->>QA: 8. Scan for 0 black frames & 0 frozen frames
    QA->>YT: 9. Resumable OAuth2 upload scheduled for 14:00 UTC (7:30 PM IST)
    YT-->>D: 10. Status 200 OK - Release Scheduled
```

---

## 3. Automation Setup: Windows Task Scheduler

To run this pipeline without manual intervention, configure a scheduled task in Windows:

### Step 1: Create the Execution Batch Script (`run_daily_autonomous.bat`)
```bat
@echo off
cd /d "C:\Users\saumy\OneDrive\Desktop\anime compiation"
"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe" scripts\engine\autonomous_channel_manager.py >> logs\autonomous_daily.log 2>&1
```

### Step 2: Register in Windows Task Scheduler (PowerShell One-Liner)
```powershell
$Action = New-ScheduledTaskAction -Execute "C:\Users\saumy\OneDrive\Desktop\anime compiation\run_daily_autonomous.bat"
$Trigger = New-ScheduledTaskTrigger -Daily -At 7:30AM
Register-ScheduledTask -TaskName "AnimeFandom_Autonomous_Shorts" -Action $Action -Trigger $Trigger -Description "Daily autonomous anime shorts producer for @animefandom0_0"
```

---

## 4. Self-Healing & Failure Safeguards
1. **WAF Fallback:** If Cloudflare triggers a CAPTCHA challenge on the primary HLS provider, the harvester automatically routes through `yt-dlp` direct micro-clipping (`--download-sections`).
2. **QA Re-Render:** If `blackdetect` fails (>0.2s black frame), the engine discards the file, shifts the start timecode by +1.0 second, and re-renders.
3. **OAuth Token Renewal:** Refresh tokens are automatically exchanged for fresh access tokens before every upload (`scripts/engine/qa_scheduler.py`), preventing authentication failures.
