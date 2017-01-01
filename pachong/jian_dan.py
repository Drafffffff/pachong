from bs4 import BeautifulSoup
import requests


def gettext(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    return soup.find('div', {'class': 'post f'}).get_text()


html = requests.get('http://jandan.net/').text
bsobj = BeautifulSoup(html, 'lxml')
total = bsobj.find_all('div', {'class': 'post f list-post'})
text = open('c://users/longfei/desktop/utl.txt', 'w')
for single in total:
    a = single.h2.a
    b = gettext(str(a['href']))
    text.write(b)
    print(b)
text.close()
