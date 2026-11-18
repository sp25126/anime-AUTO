"""
Subcategory Skill Standard Generator.
Formats all skills according to our studio reusable specification:
- YAML Frontmatter: sub_category_id, sub_category_name, niche, target_format, compositor
- Section 1: Core Narrative & Viral Philosophy (Hook -> Buildup -> Climax Clashing)
- Section 2: Reference Architecture (Canvas, Header Banner, Colors, No-Voiceover Rule)
- Section 3: Background & Orientation Protocols (Blur-Clone for Ranking, Tilt-Rotate for Cinema)
- Section 4: Dual-Tier Credit Attribution Policy (In-Video CC:@creator in Cyan #00F0FF + Description Template)
- Section 5: 5-Rank Benchmark Breakdown Table
- Section 6: Quality Assurance & Loudness Verification Gate (-14 LUFS, True Peak <= -1.5 dBTP)
"""

import os
import json

WORKSPACE = os.path.dirname(os.path.dirname(__file__))
REGISTRY_PATH = os.path.join(WORKSPACE, "src", "pipeline", "master_anime_registry.json")
SKILLS_DIR = os.path.join(WORKSPACE, "subcategory_skills")
os.makedirs(SKILLS_DIR, exist_ok=True)

def generate_standard_skills():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry = json.load(f)

    subcategories = registry.get("subcategories", {})
    niches = registry.get("core_niches", {})

    for sub_id, data in subcategories.items():
        niche_key = data.get("niche", "ranking_edits_and_moments")
        niche_info = niches.get(niche_key, {})
        composition = niche_info.get("composition", "RankingShort")
        cat_type = data.get("category_type", "action_moments")
        title_l1 = data.get("title_line1", "RANKING THE BEST")
        title_l2 = data.get("title_line2", data.get("name", "").upper())
        accent_word = data.get("accent_word", "BEST")
        accent_color = data.get("accent_color", "#FF0000")
        franchise = data.get("franchise_isolation", "Multi-Franchise")

        content = f"""---
sub_category_id: {sub_id}
sub_category_name: "{data.get('name')}"
niche: {niche_key}
category_type: {cat_type}
target_format: {composition}
channel_brand: "@animefandom0_0"
accent_color: "{accent_color}"
compositor: src/remotion/formats/{composition}.tsx
frame_rate: 30.0_cfr
resolution: 1080x1920
no_voiceovers: true
credit_attribution: mandatory_two_tier
---

# Sub-Category Skill: `{sub_id}` ("{data.get('name')}")

> **MANDATORY PRODUCTION PROTOCOL:** Subtitles are strictly disabled (`captions: []`). Dialogue voiceovers are prohibited—the narrative is carried 100% by high-energy anime soundtrack/phonk audio beds. On-screen credit tag (`CC: @creator`) in Cyan (`#00F0FF`) is required on every single clip.

---

## 1. Core Narrative & Edit Philosophy
A **"{data.get('name')}"** video captures viewer retention through visceral visual hierarchy:
* **The Hook (Rank 5 / Level 1):** Starts with an immediate high-energy visual drop to prevent swiping.
* **The Escalation (Ranks 4 ➔ 2):** Escalating intensity, faster velocity cuts, and expanding animation budget.
* **The Climax Finale (Rank 1 / Level 5):** The undisputed peak anime moment / viral edit with highest visual impact, freezing on the climax.

---

## 2. Reference Architecture & Typography
* **Canvas:** `1080x1920` (9:16 vertical), `30 fps` constant frame rate (CFR).
* **Top Pinned Header Banner:**
  * Line 1: `"{title_l1}"` (White Impact font, 78px, bold black stroke 6px).
  * Line 2: `"{title_l2}"` (Accent word: `"{accent_word}"` in `{accent_color}`).
* **Left-Side Level Progression:**
  * Rank 5: `#FFE600` (Yellow)
  * Rank 4: `#C0C0C0` (Silver)
  * Rank 3: `#FF3333` (Red)
  * Rank 2: `#FF8C00` (Orange)
  * Rank 1: `#FFD700` (Gold Climax Clashing)

---

## 3. Background & Orientation Protocol
* **Strictly Vertical for Rankings:** Rankings must never prompt for phone tilt; they remain locked in vertical 9:16 portrait.
* **Landscape to Portrait Conversion:**
  * **Blur-Clone Engine:** The 16:9 source clip is scaled to 220%, blurred (`blur(45px)`), and slightly desaturated (`saturate(0.8) brightness(0.65)`).
  * Centered foreground clip sits with a deep ambient shadow (`boxShadow: 0 0 50px rgba(0,0,0,0.85)`).

---

## 4. Dual-Tier Credit Attribution Policy
* **Tier 1 (In-Video HUD):** `CC: @creator` pinned in bold Cyan (`#00F0FF`) at the bottom center throughout the clip duration.
* **Tier 2 (YouTube Description):** Timestamped list with original editor handle, platform, source URL, anime studio, and Section 107 Fair Use legal notice.

---

## 5. 5-Rank Benchmark Breakdown Structure

| Rank | Level | Climax Arc | Pacing | On-Screen Tag | Frame Offset |
| :---: | :---: | :--- | :---: | :---: | :---: |
| **5** | Level 1 | Immediate visual hook / stylish velocity opening | 150f (5.0s) | `CC: @creator_5` | 45f impact |
| **4** | Level 2 | Creative flow escalation / unexpected choreography | 180f (6.0s) | `CC: @creator_4` | 60f impact |
| **3** | Level 3 | High-budget animation sakuga / heavy bass drop | 180f (6.0s) | `CC: @creator_3` | 75f impact |
| **2** | Level 4 | God-tier fight choreography or pure hype flex | 210f (7.0s) | `CC: @creator_2` | 90f impact |
| **1** | Level 5 | The undisputed peak viral masterpiece / climax | 240f (8.0s) | `CC: @creator_1` | 110f impact |

---

## 6. Quality Assurance & Mastering Gate
* [x] **0 Black Frames:** Automated 30fps black frame verification.
* [x] **0 Voiceover Tracks:** Audio stems are pure phonk/soundtrack beds.
* [x] **EBU R128 Loudness:** Mastered to `-14.0 ± 1.0 LUFS`, True Peak `≤ -1.5 dBTP`.
* [x] **Channel Signature:** Pinned to `@animefandom0_0`.
"""
        file_path = os.path.join(SKILLS_DIR, f"{sub_id}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"✓ Successfully generated all {len(subcategories)} skills adhering to the studio reusable standard.")

if __name__ == "__main__":
    generate_standard_skills()
