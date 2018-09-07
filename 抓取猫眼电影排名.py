import requests
import re
import json
import time
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
            }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        # 无返回对象的异常处理,仅在此处用到异常处理,处理request错误
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {  # yield生成器:循环换开始,读到第一条时,循环暂停将第一条输出,
            # 之后再进入循环读取第二条,循环停止,输出第二条,再进入循环,读取第三条,
            # 循环停止,输出第三条
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            # strip()函数表示移除字符串内指定的字符,此处为空表示移除字符串中的空格
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }

def write_to_file(content):
    with open('result.txt','a', encoding='utf-8')as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)


