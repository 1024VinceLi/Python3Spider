import urllib.request
# 方式1(GET)
# response = urllib.request.urlopen('http://www.zhihu.com')
# html = response.read()
# print(html)

# 方式2(GET)
# 请求
request = urllib.request.Request('http://www.zhihu.com')
# 响应
response = urllib.request.urlopen(request)
# 输出
html = response.read()
print(html)