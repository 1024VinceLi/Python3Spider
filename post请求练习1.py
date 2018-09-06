import urllib.parse
import urllib.request
url = 'http://www.baidu.com/s'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
postdata = {'name' : 'student',
            # 'password': 'student',
         'location' : 'SDU',
         'language' : 'Python',
         'ie' : 'utf-8',
         'wd' : 'python' }
headers = { 'User-Agent' : user_agent }
data = urllib.parse.urlencode(postdata)
#data=data.encode(encoding='UTF8')
req = urllib.request.Request(url)# 此处的Request设置参数为一个
response = urllib.request.urlopen(req)
html = response.read()
print(html.decode('UTF8'))
