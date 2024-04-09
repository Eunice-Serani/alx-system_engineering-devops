#!/usr/bin/python3
"""
This queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit

    Args:
        subreddit (str): The subreddit to query subscribers for

    Returns:
        Total subscribers, otherwise 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Chrome 121"}

    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            data = r.json()
            return data['data']['subscribers']
        return 0
    except Exception as e:
        return 0
