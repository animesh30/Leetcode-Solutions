import requests
import os
import json
import time

print("--- SCRIPT STARTING ---")

# --- CONFIG ---
USERNAME = "user9350e"
SESSION = os.environ.get('LEETCODE_SESSION')
CSRF_TOKEN = os.environ.get('LEETCODE_CSRF_TOKEN')
DIRECTORY = "solutions"

# Let's verify secrets aren't empty
if not SESSION or not CSRF_TOKEN:
    print("❌ ERROR: Secrets are missing. Check your GitHub Secrets for LEETCODE_SESSION and LEETCODE_CSRF_TOKEN.")
    exit(1)

def check_login_status():
    url = 'https://leetcode.com/graphql'
    query = "query { userStatus { isSignedIn username } }"
    headers = {
        'Cookie': f'LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': 'https://leetcode.com'
    }
    try:
        r = requests.post(url, json={'query': query}, headers=headers)
        r.raise_for_status()
        data = r.json()
        status = data.get('data', {}).get('userStatus', {})
        if status and status.get('isSignedIn'):
            print(f"✅ LOGGED IN AS: {status.get('username')}")
            return True
        print(f"❌ NOT LOGGED IN. Raw Response: {data}")
        return False
    except Exception as e:
        print(f"❌ LOGIN REQUEST FAILED: {e}")
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
        lang
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
        # Create a tiny test file just to prove the script can write
        with open(f"{DIRECTORY}/test_run.txt", "w") as f:
            f.write(f"Script ran at {time.ctime()}")

    print(f"Deep scanning {USERNAME}...")
    for offset in [0, 20, 40, 60, 80]:
        print(f"Checking offset {offset}...")
        submissions = get_submissions(offset)
        if not submissions:
            print("No submissions returned.")
            continue
            
        for sub in submissions:
            # This will show every submission the script "sees"
            print(f"Found: {sub['title']} | {sub['statusDisplay']}")
            
            if sub['statusDisplay'] == 'Accepted':
                folder_name = f"{DIRECTORY}/{sub['id']}"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    with open(f"{folder_name}/README.md", "w") as f:
                        f.write(f"# {sub['title']}\nStatus: Accepted")
                    print(f"💾 SAVED: {sub['title']}")

    print("--- SCRIPT FINISHED ---")

if __name__ == "__main__":
    main()
