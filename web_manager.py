import requests


def access_to_yahoo():
    """Yahoo! JAPANにアクセスする"""
    URL = 'https://www.yahoo.co.jp/'
    response = requests.get(URL)

    return response.text
