#!/usr/bin/python3
"""
Fetches and prints the titles of the first 10 hot posts
for a given subreddit using the Reddit API.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-agent': 'python:top-ten.hot.posts:v1.0 (by /u/ypurusername)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts:
                print(post['data'].get('title'))
        else:
            print(None)

    except Exception:
        print(None)
