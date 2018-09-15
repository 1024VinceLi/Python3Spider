import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq

base_url = 'https://m.weibo.cn/api/container/getIndex?'

def get_page(page):
    headers = {
        'host': 'm.weibo.cn',
        'Referer': 'm.weibo.cn/u/2830678474',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page  # page的动态的,作为参数传入
    }
    url = base_url + urlencode(data)
    try:
        req = requests.get(url=url, headers=headers)
        if req.status_code == 200:
            return req.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json, page: int):
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page ==1 and index ==1:
                continue
            else:
                item = item.get('mblog')
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo


if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json, page)
        for result in results:
            print(result)

