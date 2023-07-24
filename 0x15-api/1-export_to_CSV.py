#!/usr/bin/python3
""" Python script to export data in the CSV format """


import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    initial_url = "https://jsonplaceholder.typicode.com/users"
    url = initial_url + "/" + user_id

    response = requests.get(url)
    username = response.json().get('username')
    """print(username)"""

    todos_path = url + "/todos"
    response = requests.get(todos_path)
    tasks = response.json()
    """print(tasks)"""

    with open('{}.csv'.format(user_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                    .format(user_id,et username, task.get('completed'),
                    task.get('title')))
