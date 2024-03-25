#!/usr/bin/python3
"""
This implements a script that is used to export data in the JSON format.
"""
import json
import requests


def get_users(url):
    """
    Gets all users from REST API

    Args:
        url (str): Base url

    Returns:
        All users
    """
    r = requests.get(f'{url}/users')
    users = r.json()
    return users


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
    json_file = 'todo_all_employees.json'
    base_url = "https://jsonplaceholder.typicode.com"

    users = get_users(base_url)
    all_todos = {}

    for user in users:
        todos = get_todos(base_url, user.get('id'))
        todo_list = []

        for todo in todos:
            todo_list.append({
                "username": user.get('username'),
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })

        all_todos[str(user.get('id'))] = todo_list

    with open(json_file, 'w') as f:
        json.dump(all_todos, f)
