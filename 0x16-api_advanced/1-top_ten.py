#!/usr/bin/python3
'''This module defines the top_ten function
'''

import requests


def top_ten(subreddit):
    '''The function queries the Reddit API and prints the title of the
        first 10 hot posts listed for a given subreddit
    '''
    # defines the user-agent for the HTTP GET request
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # defines the URL for the http GET request
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    # defines the URL parameters for the request
    params = {'limit': 10}

    # sends the GET request
    res = requests.get(URL, headers=headers, params=params)

    if res.status_code == 200:
        try:
            data = res.json()
            posts = data.get('data').get('children')
            for post in posts:
                post_title = post.get('data').get('title')
                print(post_title)
        except Exception:
            print None
    else:
        print None
