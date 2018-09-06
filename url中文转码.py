from urllib.parse import quote, unquote
key = '壁纸'
url = 'https://www.baidu.com/s?wd='+quote(key)
print(url)
# 输出结果:  https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8
res = unquote(url)
print(res)
# 输出结果:  https://www.baidu.com/s?wd=壁纸
