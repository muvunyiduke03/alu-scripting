#!/usr/bin/python3

"""
0-subs.py

This module defines a function `number_of_subscribers` that queries
the Reddit API and returns the number of subscribers for a specified subreddit.

Author: Duke Ndamage Muvunyi
Date: 2025-06-28

Features:
- Uses Reddit's public API to fetch subscriber count.
- Gracefully handles invalid subreddits or network errors.
- Avoids following redirects to prevent false positives from search results.

Requirements:
- No authentication needed.
- Custom User-Agent required to prevent 429 (Too Many Requests) errors.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieve the total number of subscribers for a given subreddit.

    This function uses Reddit's public API endpoint:
        https://www.reddit.com/r/<subreddit>/about.json

    Parameters:
        subreddit (str): The name of the subreddit to look up.

    Returns:
        int: The number of subscribers for the subreddit.
             Returns 0 if the subreddit is invalid or inaccessible.

    Behavior:
        - Makes a GET request to the Reddit API.
        - Sets a custom User-Agent to avoid being rate-limited.
        - Does not follow redirects (invalid subreddits may redirect).
        - Returns 0 for HTTP errors, unexpected responses, or exceptions.

    Example:
        >>> number_of_subscribers("python")
        1050000

        >>> number_of_subscribers("this_subreddit_does_not_exist")
        0
    """

    # API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Define headers with a custom User-agent
    headers = {
        "User-agent": "python:subreddit.subscriber.counter:v1.0 (by /u/fakeuser123)"
    }

    try:
        # Send get request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # if the subreddit exists and data is returned
        if response.status_code == 200:
            # Extract and return the subscribr count from the response JSON
            return response.json().get("data", {}).get("subscribers", 0)
        
        return 0
    
    except requests.RequestException:
        # Handle any request-related exceptions
        return 0
