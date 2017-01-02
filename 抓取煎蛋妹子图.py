import requests
from bs4 import BeautifulSoup
import time
import os

cur_page = 1250
picture = 8662
urls = [
    'http://jandan.net/ooxx/page-{}'.format(str(i))for i in range(cur_page, 2290)]


def getImage(ads):  # 获取jpg
    global picture
    picture += 1
    '''print('Downloading...')
    name = 1;
    for imgurl in imList:
        urllib.urlretrieve(imgurl, '%s.jpg' % name)
        name += 1
    print ('Got ', len(imList), ' images')
    '''
    print('request img...')
    try:
        ir = requests.get(ads)
        print('request succeed!')
        path = os.path.dirname(__file__) + '/img/' + \
            str(picture) + '.jpg'  # 获取当前文件夹的绝对路
        print(path)
        print('Downloading ...')
        open(path, 'wb').write(ir.content)
        print('picture', picture, ' download succsed!')
    except:
        print('picture ', picture, ' download failed!')


def getGif(ads):  # 获取gif
    global picture
    picture += 1
    print('request gif...')
    try:
        ir = requests.get(ads)
        print('request succeed!')
        path = os.path.dirname(__file__) + '/img/' + \
            str(picture) + '.gif'  # 获取当前文件夹的绝对路
        print(path)
        print('Downloading ...')
        open(path, 'wb').write(ir.content)
        print('picture', picture, ' download succsed!')
    except:
        print('picture ', picture, ' download failed!')


for url in urls:
    print('-----------------page', cur_page, 'in 2290', '-----------------')
    web_date = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(web_date.text, "lxml")
    ImgUrl = soup.select('div.text > p > img')
    for i in ImgUrl:
        ads = str(i.get('src'))

        if ads.find('http:') == 0:
            pass
        else:
            ads = 'http:' + ads
        print(ads)
        if ads[-4:] == '.gif':
            getGif(ads)
        elif ads[-4:] == '.jpg':
            getImage(ads)
    cur_page += 1
