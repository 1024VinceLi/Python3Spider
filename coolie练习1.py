import http.cookiejar,urllib.request

filename = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
# 创建一个cookie对象
handler = urllib.request.HTTPCookieProcessor(cookie)
# 创建一个handler对象
opener = urllib.request.build_opener(handler)
res = opener.open('https://www.zhihu.com/')
cookie.save(ignore_discard=True, ignore_expires=True)
for item in cookie:
    print(item.name+"="+item.value)
# 打印键值对
cookie1 = http.cookiejar.LWPCookieJar()
cookie1.load('cookie.txt', ignore_expires=True, ignore_discard=True)
# 加载本地的cooki文件
handler1 = urllib.request.HTTPCookieProcessor(cookie1)# 创建对象
opener1 = urllib.request.build_opener(handler)
response = opener1.open('https://www.zhihu.com/')
print(response.read().decode('utf-8'))
# 打印网页信息