import pymongo


# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://mustafaberat:cKdwyV6BfT9XjDDp@cluster0.w72et.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

print('*'*50)

# mycollection.delete_one({"name":"Iphone 8"})
# mycollection.delete_many({"name":{"$regex":"^S"}})
result = mycollection.delete_many({}) # bütün kayıtları sil demektir
print(f' {result.deleted_count} adet kayıt silindi.')


for i in mycollection.find():
    print(i)
