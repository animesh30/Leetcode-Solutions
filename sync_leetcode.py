def get_code(submission_id):
    """Fetches the actual source code for a specific submission ID."""
    url = f"https://leetcode.com/submissions/detail/{submission_id}/check/"
    headers = {
        'Cookie': f'LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': f'https://leetcode.com/submissions/detail/{submission_id}/'
    }
    try:
        r = requests.get(url, headers=headers)
        return r.json().get('code', '')
    except:
        return ''

def main():
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    all_synced_slugs = set()
    offset = 0
    has_next = True

    while has_next and offset < 500:
        submissions, has_next = get_submissions_paginated(offset)
        if not submissions: break

        for sub in submissions:
            if sub['status_display'] == 'Accepted':
                slug = sub['title_slug']
                
                if slug not in all_synced_slugs:
                    folder_name = f"{DIRECTORY}/{slug}"
                    if not os.path.exists(folder_name):
                        os.makedirs(folder_name)
                        
                        # NEW: Fetching the actual code
                        print(f"📥 Fetching source code for: {sub['title']}")
                        code_text = get_code(sub['id'])
                        
                        # Mapping languages to extensions
                        ext_map = {'python3': 'py', 'python': 'py', 'cpp': 'cpp', 'java': 'java', 'javascript': 'js'}
                        ext = ext_map.get(sub['lang'], 'txt')
                        
                        with open(f"{folder_name}/solution.{ext}", "w") as f:
                            f.write(code_text)
                        
                        print(f"✅ Saved: {sub['title']}")
                    
                    all_synced_slugs.add(slug)
        offset += 20
        time.sleep(1) 

    print("--- ALL CODE RECOVERED ---")
