import requests
import os
import time

print("--- STARTING EMERGENCY RECOVERY ---")

# --- CONFIG ---
SESSION = os.environ.get('LEETCODE_SESSION')
CSRF_TOKEN = os.environ.get('LEETCODE_CSRF_TOKEN')
DIRECTORY = "solutions"

def get_submissions_rest():
    """Uses the Legacy REST API which bypasses some GraphQL privacy blocks."""
    url = "https://leetcode.com/api/submissions/?offset=0&limit=40"
    headers = {
        'Cookie': f'LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': 'https://leetcode.com/submissions/'
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f"❌ API Rejected Request: {r.status_code}")
            return []
        return r.json().get('submissions_dump', [])
    except Exception as e:
        print(f"❌ REST API Error: {e}")
        return []

def main():
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    # Creating a log file so your repo isn't empty if it fails
    with open(f"{DIRECTORY}/sync_log.txt", "a") as log:
        log.write(f"Attempted sync at {time.ctime()}\n")

    print("Fetching from Legacy API...")
    submissions = get_submissions_rest()
    
    if not submissions:
        print("❌ Still no submissions found. This indicates LeetCode is serving an empty list to this session.")
        return

    found_count = 0
    for sub in submissions:
        print(f"Found: {sub['title']} - {sub['status_display']}")
        if sub['status_display'] == 'Accepted':
            folder_name = f"{DIRECTORY}/{sub['title_slug']}"
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                # We save a basic file first to recover the list
                with open(f"{folder_name}/solution.txt", "w") as f:
                    f.write(f"Title: {sub['title']}\nStatus: Accepted\nID: {sub['id']}")
                found_count += 1
    
    print(f"--- FINISHED. Recovered {found_count} solutions. ---")

if __name__ == "__main__":
    main()
