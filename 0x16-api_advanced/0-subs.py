#!/usr/bin/python3
'''This module defines the number_of_subscribers function
'''

import requests


def number_of_subscribers(subreddit):
    '''The function queries the Reddit API and returns the number
        of subscribers (not active users, total subscribers) for a
        given subreddit
        If an invalid subreddit is given, return 0
    '''
    agent = 'MyRedditBot/1.0'
    # defines a custom User-Agent to avoid API rate-limiting issues
    headers = {'User-Agent': agent}

    # defines the URL for the Reddit API to get the information about
    # the subreddit
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Sends a GET rewuest to the reddit API
    res = requests.get(URL, headers, allow_redirects=False)
    if res.status_code == 200:
        payload = res.json()
        data = payload.get('data')
        return data.get('subscribers')
    return 0
