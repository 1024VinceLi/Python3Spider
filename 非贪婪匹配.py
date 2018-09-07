import re
content = 'hello 1234567 World_This is a Regex Demo'
result = re.match('^he.*?(\d+).*?Demo$', content)
print(result)# 非贪婪匹配:.*?会尽可能少的匹配字符,能交给后面匹配的就交给后面匹配
print(result.group(1))