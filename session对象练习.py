import requests
s = requests.Session()# 创建session对象
s.get('http://httpbin.org/cookies/set/name/justin')# 请求第一个网页获得cookie
r = s.get('http://httpbin.org/cookies')# 拿着第一个网页的cookie请求第二个网页
print(r.text)# r.text(文本输出)
# 输出如下:
# {
#   "cookies": {
#     "name": "justin"
#   }

