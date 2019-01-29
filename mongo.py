
from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost',27017)
#创建数据库对象
db = conn.stu

#创建集合对象
myset = db['class4']

#操作数据
# myset.insert_one({'name':'热吧','Kind':'小三'})
# myset.insert_many([{'name':'张无鸡','Kind':'倚天'},\
#                     {'name':'张三疯','Kind':'你好'}])
# myset.insert_many([{'name':'狗头','Kind':'上单'},\
#                     {'name':'后裔','Kind':'下路adc'}])
myset.save({'_id':1,'name':'郑少秋','Kind':'乾隆'})

#获取游标对象
cursor = myset.find({'name':{'$exists':True}},{'_id':0})

#循环获取每个文档
# for i in cursor:
#     print(i['name'],'---',i['Kind'])

# print(cursor.next()) #获取下一条文档

# for i in cursor.skip(1).limit(3):
#     print(i)
#注意　　排序写法同mongo shell不同，用元祖表达
# for i in cursor.sort([('name',1)]):
#     print(i)
#直接返回一个字典
# dic = {'$or':[{'name':'张无鸡'},{'Kind':'倚天'}]}
# d = myset.find_one(dic)
# print(d)

#修改操作
# myset.update_one({'kind':'上单'},{'$set'
#         :{'kind_name':'凯爹'}},upsert=True)

# myset.update_one({'kind':'下路adc'},{'$set'
#         :{'kind_name':'国服第一后裔'}},upsert=True)

#删除操作
# myset.delete_one({'Kind':'你好'})

myset.delete_many({'kind_name':{'$exists':False}})

#复合操作：
print(myset.find_one_and_delete({'name':'狗头'}))
#关闭连接
conn.close()