from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)

db = conn.image

myset = db.boy

# #读取图片
# with open('/home/tarena/dashi/timg.jpg','rb') as f:
#     data = f.read()

# #转化mongo格式
# content = bson.binary.Binary(data)

# #将内容插入集合
# doc = {'filename':'maotu.jpg','data':content}
# myset.insert_one(doc)

#获取图片
img = myset.find_one({'filename':'maotu.jpg'})

with open('/home/tarena/dashi/timg.jpg','wb') as f:
    f.write(img['data'])
conn.close()














