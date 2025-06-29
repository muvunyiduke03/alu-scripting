#!/usr/bin/python3
"""
Recursively queries the Reddit API and
returns a list of all hot article titles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively collects titles of hot articles for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): Accumulator for the titles.
        after (str): Token for the next page of results.

    Returns:
        list: List of titles if subreddit is valid, None otherwise.
    """

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-agent': 'python:hot.posts.recurs:v1.0 (by /u/yourusername)'
    }

    params = {'after':after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            return None
        
        data = response.json().get('data', {})
        posts = data.get('children', [])

        for post in posts:
            hot_list.append(post['data'].get('title'))

        after = data.get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        
        return hot_list if hot_list else None
    
    except Exception:
        return None
