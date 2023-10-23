#!/usr/bin/python3
'''Using what was done in task #0, extend your script to export
    data in json format
    Requirement:
    - Records all tasks from all employers
    - File name must be: todo_all_employers.json
'''

import json
import requests
import sys


if __name__ == '__main__':
    all_tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    all_users = requests.get(
            f'https://jsonplaceholder.typicode.com/users')

    dict_dump = {}
    for task in all_tasks.json():
        task_dict = {}
        users = [user for user in all_users.json()
                 if task.get('userId') == user.get('id')]
        task_dict["username"] = users[0].get("username")
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")

        if str(task.get('userId')) not in dict_dump:
            dict_dump[str(task.get('userId'))] = []
        dict_dump.get(str(task.get('userId'))).append(task_dict)

    filename = 'todo_all_employees.json'
    with open(filename, "w") as file:
        json.dump(dict_dump, file)
