from urllib import parse,request
url = 'http://httpbin.org/post'
headers = {'User_Agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
           'Host': 'httpbin.org'}
postdata = {'username': 'student',
            'password': 'student'}
data = bytes(parse.urlencode(postdata), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
# Request()用于添加url,data,headers,method等参数
response = request.urlopen(req)
print(response.read().decode('utf-8'))