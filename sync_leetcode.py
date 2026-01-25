import requests
import os
import json
import time

print("--- SCRIPT STARTING ---")

# --- CONFIG ---
SESSION = os.environ.get('LEETCODE_SESSION')
CSRF_TOKEN = os.environ.get('LEETCODE_CSRF_TOKEN')
DIRECTORY = "solutions"

def get_actual_username():
    """Discover the correct slug from the session."""
    url = 'https://leetcode.com/graphql'
    query = "query { userStatus { username } }"
    headers = {
        'Cookie': f'LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': 'https://leetcode.com'
    }
    r = requests.post(url, json={'query': query}, headers=headers)
    return r.json().get('data', {}).get('userStatus', {}).get('username')

def get_submissions(username, last_key=None):
    url = 'https://leetcode.com/graphql'
    headers = {
        'Cookie': f'LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': f'https://leetcode.com/u/{username}/'
    }
    # Using the exact query the LeetCode profile page uses
    query = """
    query userSubmissions($username: String!, $lastKey: String, $limit: Int) {
      submissionList(username: $username, lastKey: $lastKey, limit: $limit) {
        lastKey
        hasNext
        submissions {
          id
          title
          statusDisplay
          timestamp
          lang
        }
      }
    }
    """
    variables = {'username': username, 'limit': 20, 'lastKey': last_key}
    r = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    data = r.json()
    return data.get('data', {}).get('submissionList', {})

def main():
    username = get_actual_username()
    if not username:
        print("❌ FAILED TO DISCOVER USERNAME. Check your Session Cookie.")
        return
    print(f"✅ DISCOVERED USERNAME SLUG: {username}")

    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    last_key = None
    found_count = 0
    
    # We will check 3 pages of history
    for page in range(3):
        print(f"Scanning page {page + 1}...")
        data = get_submissions(username, last_key)
        submissions = data.get('submissions', [])
        
        if not submissions:
            print(f"No submissions found on page {page + 1}. API Response: {data}")
            break

        for sub in submissions:
            human_time = time.strftime('%Y-%m-%d', time.localtime(int(sub['timestamp'])))
            print(f"Found: {sub['title']} | {sub['statusDisplay']} | {human_time}")
            
            if sub['statusDisplay'] == 'Accepted':
                folder_name = f"{DIRECTORY}/{sub['id']}"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    with open(f"{folder_name}/README.md", "w") as f:
                        f.write(f"# {sub['title']}\nSolved on: {human_time}")
                    found_count += 1
        
        if not data.get('hasNext'):
            break
        last_key = data.get('lastKey')

    print(f"--- FINISHED. Total Saved: {found_count} ---")

if __name__ == "__main__":
    main()
