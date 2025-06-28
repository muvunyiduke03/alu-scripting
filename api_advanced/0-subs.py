#!/usr/bin/python3

"""
Module: 0-subs
This module provides a function to query the Reddit API
and return the number of subscribers for a given subreddit.

It uses Reddit's public API endpoint:
    https://www.reddit.com/r/<subreddit>/about.json

No authentication is required, but a custom User-Agent
must be set to avoid request throttling or denial.

Usage Example:
    >>> number_of_subscribers("python")
    1050000

    >>> number_of_subscribers("this_subreddit_does_not_exist")
    0
"""

import requests

def numSubscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users) for a given subreddit.

    Parameters:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers if the subreddit is valid,
             otherwise 0.

    Notes:
        - If the subreddit does not exist or an error occurs,
          the function returns 0.
        - The function avoids following redirects to prevent being
          misled by Reddit's search redirect on invalid subreddit names.
    """

    # API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Define headers with a custom User-agent
    headers = {
        "User-agent": "python:subreddit.subscriber.counter:v1.0 (by /u/fakeuser123)"
    }

    try:
        # Send GET request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # if the subreddit exists and data is returned
        if response.status_code == 200:
            # Extract and return the subscribr count from the response JSON
            return response.json().get("data", {}).get("subscribers", 0)
        
        return 0
    
    except requests.RequestException:
        # Handle any request-related exceptions
        return 0
