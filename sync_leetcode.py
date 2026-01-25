import requests
import os
import json

# Configuration
LEETCODE_SESSION = os.environ['LEETCODE_SESSION']
LEETCODE_CSRF_TOKEN = os.environ['LEETCODE_CSRF_TOKEN']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

def get_recent_submissions():
    url = 'https://leetcode.com/graphql'
    headers = {
        'Cookie': f'LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={LEETCODE_CSRF_TOKEN}',
        'X-CSRFToken': LEETCODE_CSRF_TOKEN,
        'Referer': 'https://leetcode.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    # Modern 2026 GraphQL Query
    query = """
    query getRecentSubmissionList($username: String!, $limit: Int!) {
      recentSubmissionList(username: $username, limit: $limit) {
        title
        titleSlug
        timestamp
        statusDisplay
        lang
      }
    }
    """
    
    # Note: You need your LeetCode username here
    variables = {'username': 'user9350e', 'limit': 10}
    
    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch: {response.status_code}")
        return []

    data = response.json()
    return data.get('data', {}).get('recentSubmissionList', [])

# (Logic for saving files and pushing to Git goes here)
print("Script initialized. Ready to sync.")
