from pymongo import MongoClient
from random import *

#创建数据库连接
conn = MongoClient('localhost',27017)

#创建数据库对象
db = conn.stu

#创建集合对象
myset = db['class0']
myset.delete_many({'sex':{'$exists':False}})

cursor = myset.find()
for i in cursor:
    myset.update_one({'_id':i['_id']},{'$set':{'score':{'chinese':randrange(60,100
            ),'math':randrange(60,100),'English':randrange(60,100)}}})

l = [{'$match':{'sex':'w'}},{'$sort':{'score.English':-1}},{'$project':{'_id':0}}]

cursor = myset.aggregate(l)
for i in cursor:
    print(i)


#关闭连接
conn.close()