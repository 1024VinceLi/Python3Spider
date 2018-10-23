import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.ScrapyMongoDB

collection = db.student

student = {
    'id': '1510922',
    'name': 'liweiguang',
    'time': '2018年10月22日19:22:10'
}

res = collection.insert(student)
print(res)