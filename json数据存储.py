import json
str = [{'name': 'Bob',
        '名字': '狗蛋',
        'gender': 'male',
        'birthday': '1992-10-18'}]
datas = json.dumps(str, ensure_ascii=False)
print(datas)
with open('data.txt', 'w', encoding='utf-8')as file:
    file.write(datas)

with open('datas.txt', 'w', encoding='utf-8')as f:
    f.write(json.dumps(str, indent=2, ensure_ascii=False))