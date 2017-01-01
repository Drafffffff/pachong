import requests
from bs4 import BeautifulSoup
import random
import time


def GetUrl():
    url = 'http://jandan.net/ooxx/page-' + str(random.randrange(0, 2299))
    return url


url = GetUrl()
print(url)
web_date = requests.get(url).text
print(web_date)

input("wait")
