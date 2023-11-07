#!/usr/bin/python3
'''Defines the count_words function
'''

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    '''
    '''
    # defines the URL for the HTTP GET request
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # defines the headers for the GET Request
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    # define the URL parameters for the request
    params = {'after': after}

    # sends the HTTP GET request to the REDDIT API
    res = requests.get(URL, headers=headers,
                      params=params, allow_redirects=False)
    
    # parses the response body if the response status code is 200
    if res.status_code == 200:
        payload = res.json()
        posts = payload.get('data').get('children')

        for post in posts:
            post_title = post.get('data').get('title')
            title_words_list = post_title.split()
            find_words(word_list, title_words_list, word_count)

        after = payload.get('data').get('after')
        if after:
            print(word_count)
            count_words(subreddit, word_list, after, word_count)
        
        # print(word_count)
    else:
        print(res)


def find_words(word_list, title_words_list, word_count):
    uniq_word_list = set([word.lower() for word in word_list])
    # uniq_word_list = word_list
    for word in uniq_word_list:
        for title_word in title_words_list:
            if word.lower() == title_word.lower():
                if word not in word_count:
                    word_count[word] = 0
                word_count[word] += 1
    print(title_words_list)
