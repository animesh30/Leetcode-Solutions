import requests
import os
import json
import time

# --- CONFIG ---
USERNAME = "user9350e"
SESSION = os.environ.get('LEETCODE_SESSION')
CSRF_TOKEN = os.environ.get('LEETCODE_CSRF_TOKEN')
DIRECTORY = "solutions"

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
        titleSlug
        timestamp
        statusDisplay
        lang
        id
      }
    }
    """
    variables = {'username': USERNAME, 'limit': 20, 'offset': offset}
    try:
        r = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
        return r.json()['data']['recentSubmissionList']
    except:
        return []

def main():
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    # Scans last 60 submissions to catch that 10-day-old solution
    for offset in [0, 20, 40]:
        submissions = get_submissions(offset)
        for sub in submissions:
            if sub['statusDisplay'] == 'Accepted':
                folder_name = f"{DIRECTORY}/{sub['titleSlug']}"
                file_path = f"{folder_name}/solution.txt" # Change extension based on sub['lang'] if desired

                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    # For a simple script, we save the metadata. 
                    # Getting the actual code requires a separate private API call per ID.
                    with open(file_path, "w") as f:
                        f.write(f"Problem: {sub['title']}\nLanguage: {sub['lang']}\nStatus: Accepted")
                    print(f"✅ Synced: {sub['title']}")
                else:
                    print(f"⏭️ Skipping: {sub['title']} (Already exists)")

if __name__ == "__main__":
    main()
