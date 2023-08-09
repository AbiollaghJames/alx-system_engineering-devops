#!/usr/bin/python3

import requests

# my Datadog API key
api_key = 'a6ed8e293b24be2b70ce6f32b1989f2d'

# Datadog API endpoint for dashboards
url = ' https://api.datadoghq.com/api/v1/dashboard'

# Set up headers with API key
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key
}

# Make the API request to get list of dashboards
response = requests.get(url, headers=headers)

# Parse JSON response
dashboards = response.json().get('dashboards', [])

# Find the dashboard by title (replace with your dashboard title)
my_dashboard_title = "Abiolla's Dashboard"
my_dashboard_id = None

for dashboard in dashboards:
    if dashboard['title'] == my_dashboard_title:
        my_dashboard_id = dashboard['id']
        break

if my_dashboard_id:
    print(f"The ID of '{my_dashboard_title}' dashboard is {my_dashboard_id}")
else:
    print(f"Dashboard '{my_dashboard_title}' not found.")


#https://app.datadoghq.com/dashboard/zt8-mrw-c6y?from_ts=1691559537722&to_ts=1691563137722&live=true