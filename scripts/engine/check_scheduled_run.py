import os
import sys
import json
import urllib.request
import datetime

def check_execution_status(repo: str, window_slot: str, token: str = None, current_run_id: str = None) -> bool:
    """
    Checks GitHub Actions runs to determine if the workflow has already run
    successfully during the target window for today.
    
    window_slot:
      - '1PM': checks 1:00 PM IST slot (12:00 to 17:00 IST)
      - '9PM': checks 9:00 PM IST slot (20:00 to 02:00 IST)
    
    Returns True if already run / currently running (so skip).
    Returns False if missed (needs to run now).
    """
    url = f"https://api.github.com/repos/{repo}/actions/runs?per_page=30"
    headers = {"User-Agent": "Mozilla/5.0"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
        
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            runs = data.get("workflow_runs", [])
    except Exception as e:
        print(f"[Jitter Guard] Warning: Failed to query GitHub API: {e}. Proceeding with production.")
        return False

    now_utc = datetime.datetime.now(datetime.timezone.utc)
    now_ist = now_utc + datetime.timedelta(hours=5, minutes=30)
    today_date = now_ist.date()

    curr_id_str = str(current_run_id) if current_run_id else None

    for r in runs:
        run_id_str = str(r.get("id"))
        
        # CRITICAL: Ignore the current running workflow execution so it does not check itself!
        if curr_id_str and run_id_str == curr_id_str:
            continue

        status = r.get("status")
        # Check if an earlier run is actively running right now
        if status in ["in_progress", "queued"]:
            print(f"[Jitter Guard] Parallel run {r.get('id')} is currently {status}. Skipping to avoid duplicate overlap.")
            return True

        # Check if already successfully finished for the window today
        if r.get("conclusion") == "success":
            created = datetime.datetime.fromisoformat(r["created_at"].replace("Z", "+00:00"))
            created_ist = created + datetime.timedelta(hours=5, minutes=30)
            
            # Check if created on the same calendar day (IST)
            if created_ist.date() == today_date:
                h = created_ist.hour
                if window_slot == "1PM" and (12 <= h < 17):
                    print(f"[Jitter Guard] ✅ 1:00 PM IST slot already completed today by run {r.get('id')} at {created_ist.strftime('%H:%M IST')}.")
                    return True
                elif window_slot == "9PM" and (20 <= h <= 23 or h == 0 or h == 1):
                    print(f"[Jitter Guard] ✅ 9:00 PM IST slot already completed today by run {r.get('id')} at {created_ist.strftime('%H:%M IST')}.")
                    return True

    print(f"[Jitter Guard] ⚡ No completed execution detected for {window_slot} slot today. Triggering production!")
    return False

if __name__ == "__main__":
    slot = sys.argv[1] if len(sys.argv) > 1 else "1PM"
    repo = os.environ.get("GITHUB_REPOSITORY", "sp25126/anime-AUTO")
    token = os.environ.get("GITHUB_TOKEN", None)
    current_run_id = os.environ.get("GITHUB_RUN_ID", None)
    
    already_ran = check_execution_status(repo, slot, token, current_run_id)
    
    # Write output variable for GitHub Actions step
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"should_run={'false' if already_ran else 'true'}\n")
    else:
        print(f"Result: should_run = {'false' if already_ran else 'true'}")
