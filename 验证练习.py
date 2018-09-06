from urllib.request import HTTPPasswordMgrWithDefaultRealm, build_opener,HTTPBasicAuthHandler
from urllib.error import URLError
username = 'username'
password = 'password'
url = 'http://baidu.com'
p = HTTPPasswordMgrWithDefaultRealm()
# 创建密码管理对象
p.add_password(None, url, username, password)
# 密码管理对象添加url和账号密码
hander = HTTPBasicAuthHandler(p)
# 创建验证管理对象hander,并传去参数密码管理对象
opener = build_opener(hander)
# 创建opener并传入验证管理对象
try:
    res = opener.open(url)# 使用opener的open方法进入url
    html = res.read().decode('utf-8')
    print(res.status)# 打印状态码
    print(html)# 打印最终网页数据

except URLError as e:
     print(e.reason)
