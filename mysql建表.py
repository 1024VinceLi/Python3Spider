import pymysql
db = pymysql.connect(host='localhost', user='root', password='1308310285', port=3306, db='spider')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id , name , age , PRIMAPY KEY (id)) VALUES (%s, %s, %s)'
cursor.execute(sql, ('Bob', '20', '20120001'))
db.close()