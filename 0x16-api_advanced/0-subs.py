#!/usr/bin/python3
""" Get total number of subs"""


import requests


def number_of_subscribers(subreddit):
    """ Return subs of given subreddit """
    baseurl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "Fake-Agent"}
    response = requests.get(baseurl, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        subs = response.json().get('data').get('subscribers')
    else:
        subs = 0
    return subs