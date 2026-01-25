import requests
import os
import time

print("--- FULL CODE SYNC STARTING ---")

# --- CONFIG ---
SESSION = os.environ.get('LEETCODE_SESSION')
CSRF_TOKEN = os.environ.get('LEETCODE_CSRF_TOKEN')
DIRECTORY = "solutions"

# Language to Extension Mapper
EXTENSIONS = {
    'python': 'py', 'python3': 'py', 'cpp': 'cpp', 
    'java': 'java', 'javascript': 'js', 'typescript': 'ts',
    'csharp': 'cs', 'ruby': 'rb', 'swift': 'swift', 'golang': 'go'
}

def get_actual_code(submission_id):
    """Fetches the actual source code text for a submission."""
    # This is the 2026 endpoint for grabbing the raw code
    url = f"https://leetcode.com/submissions/detail/{submission_id}/check/"
    headers = {
        'Cookie': f'LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': f'https://leetcode.com/submissions/detail/{submission_id}/'
    }
    try:
        r = requests.get(url, headers=headers)
        return r.json().get('code', 'Code not found.')
    except:
        return 'Error fetching code.'

def get_submissions(offset=0):
    url = f"https://leetcode.com/api/submissions/?offset={offset}&limit=20"
    headers = {
        'Cookie': f'LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': 'https://leetcode.com/submissions/'
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        return data.get('submissions_dump', []), data.get('has_next', False)
    return [], False

def main():
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    all_synced_slugs = set()
    offset = 0
    has_next = True
    total_saved = 0

    while has_next and offset < 500:
        print(f"Checking submissions {offset} to {offset + 20}...")
        submissions, has_next = get_submissions(offset)
        
        if not submissions:
            break

        for sub in submissions:
            if sub['status_display'] == 'Accepted':
                slug = sub['title_slug']
                
                if slug not in all_synced_slugs:
                    folder_name = f"{DIRECTORY}/{slug}"
                    lang = sub['lang']
                    ext = EXTENSIONS.get(lang, 'txt')
                    file_path = f"{folder_name}/solution.{ext}"

                    # If folder exists but NO code file exists, we fetch it
                    if not os.path.exists(file_path):
                        if not os.path.exists(folder_name):
                            os.makedirs(folder_name)
                        
                        print(f"📥 Fetching code: {sub['title']} ({lang})")
                        raw_code = get_actual_code(sub['id'])
                        
                        with open(file_path, "w") as f:
                            f.write(raw_code)
                        total_saved += 1
                        time.sleep(1) # Safety delay for the extra API call
                    
                    all_synced_slugs.add(slug)

        offset += 20

    print(f"--- FINISHED ---")
    print(f"Unique problems processed: {len(all_synced_slugs)}")
    print(f"New source code files created: {total_saved}")

if __name__ == "__main__":
    main()
