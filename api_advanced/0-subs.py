#!/usr/bin/python3
"""
This module contains a function to query the Reddit API for subreddit subscribers.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The total number of subscribers for the subreddit, or 0 if invalid.
    """
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to avoid Too Many Requests errors
    # Reddit API best practices recommend a unique and descriptive User-Agent.
    headers = {
        "User-Agent": "MyRedditApp/1.0 (by YourUsername)"
    }

    try:
        # Make the GET request to the Reddit API
        # Set allow_redirects=False to ensure we do not follow redirects,
        # which can happen for invalid subreddits (redirecting to search).
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200 OK)
        if response.status_code == 200:
            data = response.json()
            # The number of subscribers is typically found under data['data']['subscribers']
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            # If the status code is not 200 (e.g., 404 Not Found for invalid subreddits,
            # or a redirect status like 302 found), return 0.
            return 0
    except requests.exceptions.RequestException:
        # Handle network-related errors (e.g., connection errors, timeouts)
        return 0
    except ValueError:
        # Handle JSON decoding errors (if the response is not valid JSON)
        return 0
    except Exception:
        # Catch any other unexpected errors and return 0
        return 0

