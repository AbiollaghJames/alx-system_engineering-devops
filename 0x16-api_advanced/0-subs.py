#!/usr/bin/python3
""" Script to get total number of subs """


def number_of_subscribers(subreddit):
    """ Return subs of given subreddit """

    import requests

    baseurl = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "Fake-Agent"}
    response = requests.get(baseurl, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        subs = response.json().get('data').get('subscribers')
    else:
        subs = 0
    return subs