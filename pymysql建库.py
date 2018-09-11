import pymysql
str = [{'name': 'Bob',
        '名字': '狗蛋',
        'gender': 'male',
        'birthday': '1992-10-18'}]
db = pymysql.connect(host='localhost', user='root', password='1308310285', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spider DEFAULT CHARACTER SET utf8")
db.close()