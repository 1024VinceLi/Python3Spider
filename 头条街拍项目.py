import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool # 最后一个是大写的P

def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': True,
        'count': '20'
    }
    url = 'http://www.toutiao.com/search_countent/?' + urlencode(params)
    try:
        req = requests.get(url)
        if req.status_code == 200:
            return req.json()
    except requests.ConnectionError as e:
        print(e.args)

def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_delail')
            for image in images:
                yield {
                    'image': image.get('url'),
                    'title': title
                }

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        res = requests.get(item.get('title'))
        if res.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(res.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb')as f:
                    f.write(res.content)
            else:
                print('Already Download', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset=offset)
    for item in get_image(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x*20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()