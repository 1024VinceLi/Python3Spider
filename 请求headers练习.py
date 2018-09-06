import urllib.parse
import urllib.request
url = 'https://www.sogo.com/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer = 'https://www.baidu.com/'
postdata = {'username': 'student', 'password': 'student', 'wd': 'python' }
headers = {'User_Agent': user_agent, 'Referer': referer}
data = urllib.parse.urlencode(postdata)
req = urllib.request.Request(url)
# 添加头信息
req.add_header('User_Agent', user_agent)
req.add_header('Referer', referer)
req.add_header('data', data)
response = urllib.request.Request(url)
res = urllib.request.urlopen(response)
html = res.read()# 读取网页信息(read函数没有参数)
print(html.decode('utf8'))
