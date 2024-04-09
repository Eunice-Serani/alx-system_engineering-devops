#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords
"""
from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords

    Args:
        subreddit (str): The name of the subreddit to query
        hot_list (list of str): A list of keywords to count occurrences of
        after (str): A token indicating the last post retrieved in pagination
        counts (Counter): A Counter object to store the counts of keywords

    Returns:
        None. Prints the sorted count of keywords.

    Note:
    - If word_list contains the same word (case-insensitive), the final count
    should be the sum of each duplicate.
    - Results should be printed in descending order, by the count, and if the
    count is the same for separate keywords, they should then be sorted
    alphabetically (ascending, from A to Z).
    - Words with no matches are skipped and not printed.
    - Results are based on the number of times a keyword appears, not titles
    it appears in.
    - Words such as "java.", "java!", or "java_" should not count as "java".
    """
    if counts is None:
        counts = Counter()

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {"User-Agent": "Chrome 121"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            for child in children:
                title = child['data']['title']
                for word in word_list:
                    if word.lower() in title.lower().split():
                        counts[word.lower()] += 1
            after = data['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(
                    counts.items(),
                    key=lambda x: (-x[1], x[0])
                    )
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        elif response.status_code == 404:
            return
        else:
            return
    except Exception as e:
        print("Error:", e)
        return
