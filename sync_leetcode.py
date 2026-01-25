import requests
import os
import json
import time

# --- CONFIG ---
USERNAME = "user9350e"
SESSION = os.environ.get('LEETCODE_SESSION')
CSRF_TOKEN = os.environ.get('LEETCODE_CSRF_TOKEN')
DIRECTORY = "solutions"

def check_login_status():
    """Verify if the cookies actually log us in."""
    url = 'https://leetcode.com/graphql'
    query = "query { user { username isVerified isSignedIn } }"
    headers = {
        'Cookie': f'LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': 'https://leetcode.com'
    }
    try:
        r = requests.post(url, json={'query': query}, headers=headers)
        data = r.json()
        user = data.get('data', {}).get('user', {})
        if user.get('isSignedIn'):
            print(f"✅ SUCCESSFULLY LOGGED IN AS: {user.get('username')}")
            return True
        else:
            print("❌ LOGIN FAILED: The cookies you provided do not show a signed-in session.")
            print(f"DEBUG DATA: {data}")
            return False
    except Exception as e:
        print(f"❌ CONNECTION ERROR: {e}")
        return False

def get_submissions(offset=0):
    url = 'https://leetcode.com/graphql'
    headers = {
        'Cookie': f'LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': 'https://leetcode.com'
    }
    query = """
    query memberRecentSubmissions($username: String!, $limit: Int!, $offset: Int!) {
      recentSubmissionList(username: $username, limit: $limit, offset: $offset) {
        title
        timestamp
        statusDisplay
        id
      }
    }
    """
    variables = {'username': USERNAME, 'limit': 20, 'offset': offset}
    r = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    return r.json().get('data', {}).get('recentSubmissionList', [])

def main():
    if not check_login_status():
        return

    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    print(f"Deep scanning submissions for {USERNAME}...")
    found_count = 0
    
    # Scanning 100 submissions to be absolutely sure we hit 10 days ago
    for offset in [0, 20, 40, 60, 80]:
        submissions = get_submissions(offset)
        if not submissions:
            print(f"No submissions found at offset {offset}.")
            continue
            
        for sub in submissions:
            # Print EVERY submission found to the log for debugging
            human_time = time.strftime('%Y-%m-%d', time.localtime(int(sub['timestamp'])))
            print(f"Found: {sub['title']} | Status: {sub['statusDisplay']} | Date: {human_time}")
            
            if sub['statusDisplay'] == 'Accepted':
                folder_name = f"{DIRECTORY}/{sub['id']}" # Using ID to avoid slug errors
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    with open(f"{folder_name}/README.md", "w") as f:
                        f.write(f"# {sub['title']}\nSolved on: {human_time}")
                    found_count += 1

    print(f"Total new solutions saved: {found_count}")

if __name__ == "__main__":
    main()
