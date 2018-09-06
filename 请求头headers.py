import urllib.parse
import urllib.request
url = 'http://www.baidu.com/s'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# 用户代理
referer = 'https://www.sogo.com/'
# Referer是header的一部分，当浏览器向web服务器发送请求的时候，
# 一般会带上Referer，告诉服务器我是从哪个页面链接过来的，
# 服务器籍此可以获得一些信息用于处理。
postdata = {'name': 'student',
            'location': 'SDU',
            }
headers = {'user_agent': user_agent, 'Referer': referer}
# headers = {用户代理, 发出请求的地址}
data = urllib.parse.urlencode(postdata)
# 转换url编码
req = urllib.request.Request(url)
req.add_header('User_Agent', user_agent)
req.add_header('Referer', referer)
req.add_header('data', data)
response = urllib.request.urlopen(req)
# 响应接收
html = response.read()
print(html.decode('utf-8'))
# 打印
