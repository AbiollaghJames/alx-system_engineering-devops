#!/usr/bin/python3
""" Python script that returns information about employee todo list progress """


import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    initial_url = "https://jsonplaceholder.typicode.com/users"
    url = initial_url + "/" + employee_id

    response = requests.get(url)
    todolist_data = response.json()
    ###print(todolist_data)

    e_name = todolist_data.get("name", "")
    all_tasks = len(todolist_data.get("tasks", []))
    done_tasks = sum(1 for task in todolist_data.get("tasks", []) if tasks.get("completed"))

    print("Employee {} is done with tasks({} / {}):".format(e_name, done_tasks, all_tasks))

    for task in todolist_data.get("tasks", []):
        if tasks.get("completed"):
            print("\t {}".format(task.get('title')))
