#!/usr/bin/python3
"""
Recursive function to count keywords in hot post titles of a subreddit
"""

import requests

def count_word(subreddit, word_list, hot_list=[], after=None, word_count=None):
    if word_count is None:
        # Normalize word list to lowercase and sum duplicates
        word_count = {}
        for word in word_list:
            key = word.lower()
            word_count[key] = word_count.get(key, 0) + 0

    headers = {'User-agent': 'python:keyword.counter:v1.0 (by /u/fakeuser)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return
    
    data = response.json().get('data', {})
    posts = data.get('children', [])
    after = data.get('after', None)

    for post in posts:
        title = post['data']['title'].lower().split()
        for word in word_count.keys():
            word_count[word] += title.count(word)

    if after is not None:
        return count_word(subreddit, word_list, hot_list, after, word_count)
    
    # print results
    filtered = {k: v for k, v in word_count.items() if v > 0}
    for word in sorted(filtered.items(), key=lambda x: (-x[1], x[0])):
        print(f"{word[0]}: {word[1]}")