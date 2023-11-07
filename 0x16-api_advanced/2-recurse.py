#!/usr/bin/python3
'''Defines the recurse function
'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    '''The recursive function queries the Reddit API and returns a
        list containing the titles of all hot articles for a given
        subreddit.

        If no results were found for the given subreddit, return None
    '''
    # defines the URL for the HTTP GET request
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # defines the headers for the GET Request
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    # define the URL parameters for the request
    params = {'after': after}

    # sends a GET request to the Reddit API
    res = requests.get(URL, headers=headers, params=params)
    if res.status_code == 200:
        try:
            # parse the JSON response of the URL request
            payload = res.json()
            posts = payload.get('data').get('children')

            for post in posts:
                post_title = post.get('data').get('title')
                hot_list.append(post_title)

            # checks if there are more pages to retrieve
            after = payload.get('data').get('after')
            if after:
                # Recursively call the function to get the next page
                # if it exists
                recurse(subreddit, hot_list, after)
            # returns the hot_list if there is no more next page
            return hot_list
        except Exception:
            return hot_list

    return None
