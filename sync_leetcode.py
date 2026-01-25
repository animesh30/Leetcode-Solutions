import requests
import os
import time

print("--- STARTING FULL HISTORY SYNC ---")

# --- CONFIG ---
SESSION = os.environ.get('LEETCODE_SESSION')
CSRF_TOKEN = os.environ.get('LEETCODE_CSRF_TOKEN')
DIRECTORY = "solutions"

def get_submissions_paginated(offset=0):
    """Fetches a specific page of submissions."""
    url = f"https://leetcode.com/api/submissions/?offset={offset}&limit=20"
    headers = {
        'Cookie': f'LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': 'https://leetcode.com/submissions/'
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            return data.get('submissions_dump', []), data.get('has_next', False)
        return [], False
    except:
        return [], False

def main():
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    all_synced_slugs = set()
    offset = 0
    has_next = True
    total_found = 0

    # This loop keeps going until LeetCode says there are no more submissions
    while has_next and offset < 500: # Safety cap at 500 submissions
        print(f"Checking submissions {offset} to {offset + 20}...")
        submissions, has_next = get_submissions_paginated(offset)
        
        if not submissions:
            break

        for sub in submissions:
            if sub['status_display'] == 'Accepted':
                slug = sub['title_slug']
                
                # Check if we already processed this problem in this run
                if slug not in all_synced_slugs:
                    folder_name = f"{DIRECTORY}/{slug}"
                    if not os.path.exists(folder_name):
                        os.makedirs(folder_name)
                        with open(f"{folder_name}/solution.txt", "w") as f:
                            # Note: To get the FULL code, we'd need another API call, 
                            # but let's first get your directory structure back.
                            f.write(f"Title: {sub['title']}\nLanguage: {sub['lang']}")
                        print(f"✅ New problem found: {sub['title']}")
                        total_found += 1
                    
                    all_synced_slugs.add(slug)

        offset += 20
        time.sleep(1) # Small delay to avoid being rate-limited

    print(f"--- SYNC COMPLETE ---")
    print(f"Total unique problems in 'solutions' folder: {len(all_synced_slugs)}")
    print(f"New problems added in this run: {total_found}")

if __name__ == "__main__":
    main()
