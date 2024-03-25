#!/usr/bin/python3
"""
This implements a script that is used to export data in the JSON format.
"""
import json
import requests
import sys


def get_username(url, uid):
    """
    Gets the username from REST API

    Args:
        url (str): Base url
        user_id (int): The id of the user

    Returns:
        User name
    """
    r = requests.get(f'{url}/users/{uid}')
    user = r.json()
    return user.get('username')


def get_todos(url, uid):
    """
    Gets the todos for a particular user from REST API

    Args:
        url (str): Base url
        user_id (int): The id of the user

    Returns:
        Todos
    """
    r = requests.get(f'{url}/todos?userId={uid}')
    todos = r.json()
    return todos


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_name = get_username(base_url, user_id)
    todos = get_todos(base_url, user_id)
    todo_list = []

    for todo in todos:
        todo_list.append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user_name
        })

    with open(f'{user_id}.json', 'w') as json_file:
        json.dump({str(user_id): todo_list}, json_file)
