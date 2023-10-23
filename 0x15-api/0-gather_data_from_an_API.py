#!/usr/bin/python3
'''The python script gets data from a REST API for a given
    employee ID and returns information about his/her TODO
    list progress
'''

import requests
import sys


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        user_id = int(sys.argv[1])
        all_tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
        user = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
        total_tasks_by_user_id = [task for task in all_tasks.json()
                                       if user_id == task.get('userId')]
        tasks_done_by_user_id = [task for task in total_tasks_by_user_id
                                        if task.get('completed') == True]

        print("Employee {} is done with tasks({}/{}):".format(
            user.json().get('name'),
            len(tasks_done_by_user_id),
            len(total_tasks_by_user_id)
        ))
        for task in tasks_done_by_user_id:
            print("\t {}".format(task.get("title")))
