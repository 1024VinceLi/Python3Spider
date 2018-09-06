from urllib.parse import urlparse
res = urlparse('http://www.baidu.com/index.html;user?di=5#comment', allow_fragments=False)
# 设置为False忽略所有锚点
print(res.scheme, res[0], res[1], res.netloc, sep='\n')
# 可以使用索引选择,也可以用属性名选择性提取信息