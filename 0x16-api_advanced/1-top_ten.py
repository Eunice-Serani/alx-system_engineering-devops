#!/usr/bin/python3
"""
Queries the Reddit API and prints titles of the first 10 hot posts listed
for a given subreddit
"""
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints titles of the first 10 hot posts
    listed for a given subreddit

    Args:
        subreddit (str): The subreddit to get titles from
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Chrome 121"}

    r = requests.get(url=url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        subs = r.json()
        for data in subs.get('data').get('children'):
            print(data.get('data').get('title'))
    else:
        print(None)
