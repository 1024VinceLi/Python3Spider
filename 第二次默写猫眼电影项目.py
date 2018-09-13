import requests
import re
import json
import time
# 1.请求网站
def get_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
            }
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        return res.text
    return None

# 2.解析网站
def parse_page(html):
    parttern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(parttern, html)
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
        print(item)

# 3.写入本地
def wirte_page(content):
    with open('result3.txt', 'a', encoding='utf-8')as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


# 4.主函数
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_page(url)
    for item in parse_page(html):
        print(item)
        wirte_page(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)

