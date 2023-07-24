#!/usr/bin/python3
""" Python script to export data in the CSV format """



import csv
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    initial_url = "https://jsonplaceholder.typicode.com/users"
    url = initial_url + "/" + user_id

    response = requests.get(url)
    username = response.json().get('username')

    todos = url + "/todos"
    response = requests.get(todos)
    tasks = response.json()

    with open('{}.csv'.format(user_id), 'w') as csv_file:
        for task in tasks:
            csv_file.write("'{}' '{}', '{}'".format(
                user_id, username, task.get('completed'),
                    task.get('title')))
