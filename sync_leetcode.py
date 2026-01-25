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
    """Verify if the cookies actually log us in using the 2026 schema."""
    url = 'https://leetcode.com/graphql'
    # Updated GraphQL query for 2026
    query = """
    query {
      userStatus {
        isSignedIn
        username
      }
    }
    """
    headers = {
        'Cookie': f'LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': 'https://leetcode.com'
    }
    try:
        r = requests.post(url, json={'query': query}, headers=headers)
        data = r.json()
        status = data.get('data', {}).get('userStatus', {})
        
        if status.get('isSignedIn'):
            print(f"✅ SUCCESSFULLY LOGGED IN AS: {status.get('username')}")
            return True
        else:
            print("❌ LOGIN FAILED: Your session cookie is invalid or expired.")
            print(f"DEBUG: Ensure your LEETCODE_SESSION secret is correct.")
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
    # Checking 100 entries to find that 10-day-old solution
    for offset in [0, 20, 40, 60, 80]:
        submissions = get_submissions(offset)
        if not submissions:
            continue
            
        for sub in submissions:
            if sub['statusDisplay'] == 'Accepted':
                folder_name = f"{DIRECTORY}/{sub['id']}"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    with open(f"{folder_name}/README.md", "w") as f:
                        f.write(f"# {sub['title']}\nID: {sub['id']}")
                    print(f"✅ Synced: {sub['title']}")
