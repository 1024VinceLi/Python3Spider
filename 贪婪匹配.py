import re
content = 'hello 1234567 World_This is a Regex Demo'
result = re.match('^he.*(\d+).*Demo$', content)
print(result)# 贪婪匹配:第一组.*会尽可能的匹配更多的字符,只给后面留下唯一可匹配的
print(result.group(1))