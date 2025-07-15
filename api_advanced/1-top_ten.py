#!/usr/bin/python3
"""documenting stuff"""
import requests


def top_ten(subreddit):
    """Docs"""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozzilla/5.0'}
    params = {'limit': 10}

    response = requests.get(
        reddit_url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return
    
    try:
        data =response.json().get('data', {}).get('children', [])
        if not data:
            print(None)
            return
        for post in data[:10]:
            print(post['data']['title'])

    except Exception:
        print(None)
