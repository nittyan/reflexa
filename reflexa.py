#-*- coding:utf-8 -*-

import urllib
import urllib2
import json


URL = 'http://labs.preferred.jp/reflexa/api.php?'


def search(word):
    '''
    Args:
        word: string
    Returns:
        array<string>
    '''
    url = URL + create_parameter(word)
    response = urllib2.urlopen(url)
    json_response = json.load(response)

    return json_response


def create_parameter(word):
    query = {
        'q': word.encode('utf-8'),
        'format': 'json'
    }
    return urllib.urlencode(query)

if __name__ == '__main__':
    result = search(u'カメ')
    for r in result:
        print(r)
