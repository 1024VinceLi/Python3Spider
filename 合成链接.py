from urllib.parse import urlunparse
data = ['https', 'www.zhihu.com', 'index.html', 'user', 'id=5', 'comment']
res = urlunparse(data)
print(res)