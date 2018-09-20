import requests
import re
import json


def get_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
             }
    try:
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            return req.text
    except requests.RequestException:
        print(None)



def parse_page(html):
    parttener = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(parttener, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            # strip()函数表示移除字符串内指定的字符,此处为空表示移除字符串中的空格
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

def write_page(data):
    with open('result6.txt', 'a' , encoding='utf-8')as f:
        f.write(json.dumps(data))


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_page(url)
    for item in parse_page(html):
        print(item)
        write_page(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
