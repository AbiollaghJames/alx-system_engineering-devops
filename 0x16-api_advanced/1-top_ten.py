#!/usr/bin/python3
""" Script to list first 10 hot posts for a subreddit """

import requests


def top_ten(subreddit):
    """ Prints titles of first 10 hot posts """

    baseurl = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "Fake-Agent"}
    response = requests.get(baseurl, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        i = 0
        for i in response.json().get('data').get('children'):
            print(i.get('data').get('title'))
            i += 1
            if i >= 10:
                break
        status = 1
    else:
        print("None")
        status = 0

    return status