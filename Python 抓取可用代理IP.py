"""
该程序用于从代理网站获取可用ip
使用方法1： 直接运行该文件，会在同目录下生成ips.txt文件，文件内包含可用的代理
使用方法2： 其他程序导入该文件，然后直接使用该文件内定义的全局变量'proxies'
"""
import random
import threading
import time
from concurrent import futures

import requests
from pyquery import PyQuery

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                  Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2306.400 QQBrowser/9.5.10530.400'}
# 检测代理ip有效性的网站
CHECK_URL = 'https://ip.cn'
# 抓取地址(西刺代理)
FETCH_URL = 'http://www.xicidaili.com/wn/{}'
# 抓取页数，每页100条
PAGES = 3
# 代理类型（http/https）
PROXY_HTTPS = 'https'
PROXY_HTTP = 'http'
# 有效代理ip列表
proxies_http = []
proxies_https = []
# 线程池，用于同时验证多个代理ip
POOL = futures.ThreadPoolExecutor(max_workers=50)
# 理解为一个在未来完成的操作，这是异步编程的基础




def fetch_proxy():
    """
    抓取代理ip
    :return:
    """
    for page in range(1, PAGES + 1):
        r = requests.get(FETCH_URL.format(page), headers=headers)
        doc = PyQuery(r.content.decode('utf-8'))
        # 获取数据列表对应的table
        table = doc('#ip_list')
        # 获取table中除了表头以外的所有行
        rows = table('tr:nth-of-type(n+2)').items() # nth-of-type(n+2)表示提取tr的父元素中所包含的全部tr的第2个到第n个
        # 提取每一行中的ip和端口号
        for row in rows: # nth-of-type//css选择器
            ip = row('td:nth-of-type(2)').text() # td:nth-of-type(2)表示td的父元素所包含的第2个td
            port = row('td:nth-of-type(3)').text()
            proxy = ip + ':' + port
            # 在线程池中检测该代理是否可用
            POOL.submit(add_proxy, proxy)
        # 10秒钟后抓取下一页
        time.sleep(10)




def add_proxy(proxy: str):
    """
    添加代理
    :param proxy: 代理ip+端口号
    :return:
    """
    try:
        r = requests.get(CHECK_URL, proxies={PROXY_HTTP: proxy}, timeout=50)
        print(PyQuery(r.content.decode()).find('#result').text(), '\n')
        if r.status_code == 200 and proxy not in proxies_http:
            proxies_http.append(proxy)
    except Exception as e:
        if proxy in proxies_http:
            proxies_http.remove(proxy)
        print(e.args)
    try:
        req = requests.get(CHECK_URL, proxies={PROXY_HTTPS: proxy}, timeout=50)
        print(PyQuery(req.content.decode()).find('#result').text(), '\n')
        if req.status_code == 200 and proxy not in proxies_https:
            proxies_https.append(proxy)
    except Exception as e:
        if proxy in proxies_https:
            proxies_https.remove(proxy)
        print(e.args)




def run():
    while True:
        try:
            fetch_proxy()
            print('HTTP有效代理：', proxies_http)
            print('HTTPS有效代理：', proxies_https)
            # 将有效代理写入文件
            with open('ips_http.txt', 'w', encoding='utf-8') as f:
                f.write('\nHTTP_'.join(proxies_http)) # '\n'.join(proxies)以\n作为分隔符，将proxies所有的元素合并成一个新的字符串
            with open('ips_https.txt', 'w', encoding='utf-8') as fl:
                fl.write('\nHTTPS_'.join(proxies_https))
        except Exception as e:
            print(e)
        # 抓取一次之后休息一段时间，防止被屏蔽
        time.sleep(random.randint(100, 600))


# 启动抓取线程
threading.Thread(target=run).start()
# target 是被 run()方法调用的回调对象. 默认应为None, 意味着没有对象被调用。
