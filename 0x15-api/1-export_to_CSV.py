#!/usr/bin/python3
"""
This implements a script that is used to export data in the CSV format.
"""
import csv
import requests
import sys


def get_username(url, user_id):
    """
    Gets the username from REST API

    Args:
        url (str): Base url
        user_id (int): The id of the user

    Returns:
        User name
    """
    r = requests.get(f'{url}/users/{user_id}')
    user = r.json()
    return user.get('username')


def get_todos(url, user_id):
    """
    Gets the todos for a particular user from REST API

    Args:
        url (str): Base url
        user_id (int): The id of the user

    Returns:
        Todos
    """
    r = requests.get(f'{url}/todos?userId={user_id}')
    todos = r.json()
    return todos


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_name = get_username(base_url, user_id)
    todos = get_todos(base_url, user_id)

    with open(f'{user_id}.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [user_id, user_name, todo.get('completed'), todo.get('title')]
            )
