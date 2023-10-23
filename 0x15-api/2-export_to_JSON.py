#!/usr/bin/python3
'''The script extends what was done in task #0 to export data
    in json format
    Requirement:
    - Records all tasks owned by this employee
    - File name must be: USER_ID.json
'''

import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        user_id = int(sys.argv[1])
        all_tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
        user = requests.get(
                f'https://jsonplaceholder.typicode.com/users/{user_id}')
        total_tasks_by_user_id = [task for task in all_tasks.json()
                                  if user_id == task.get('userId')]
        dict_dump = {}
        for task in total_tasks_by_user_id:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = user.json().get("username")
            if str(user_id) not in dict_dump:
                dict_dump[str(user_id)] = []
            dict_dump.get(str(user_id)).append(task_dict)

        filename = f'{user_id}.json'
        with open(filename, "w") as file:
            json.dump(dict_dump, file)
