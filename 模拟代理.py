# 代码验证失败,暂时没有可用的代理IP
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
proxy = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1.9743'
})
opener = build_opener(proxy)
try:
    res = opener.open('https://baidu.com')
    print(res.read().decode('utf-8'))
except URLError as e:
    print(e.reason)