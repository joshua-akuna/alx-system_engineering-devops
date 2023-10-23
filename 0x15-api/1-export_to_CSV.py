#!/usr/bin/python3
'''The python script gets data from a REST API for a given
    employee ID and returns information about his/her TODO
    list progress
'''
import csv
import requests
import sys


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        user_id = int(sys.argv[1])
        all_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos')
        user = requests.get(
                f'https://jsonplaceholder.typicode.com/users/{user_id}')
        tasks_by_user_id = [task for task in all_tasks.json()
                            if user_id == task.get('userId')]
        filename = f'{user_id}.csv'
        username = user.json().get('username')

        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in tasks_by_user_id:
                u_id = str(user_id)
                status = str(task.get('completed'))
                title = task.get('title')
                csvwriter.writerow([u_id, username, status, title])
