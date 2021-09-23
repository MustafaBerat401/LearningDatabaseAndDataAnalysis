import pymongo


# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://mustafaberat:cKdwyV6BfT9XjDDp@cluster0.w72et.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)
print('****************')

# update_one => sadece bir kaydı günceller
# mycollection.update_one(
#     {'name':'Samsung S6'},
#     {'$set':{
#         'name':'Iphone 7',
#         'price': 5000
#     }}
# )

# for i in mycollection.find():
#     print(i)

# update_many => birden fazla güncelleme işlemi yapar
query = {'name':'Samsung S7'}
newvalues = {'$set': {
            'name':'Iphone 8',
            'price': 5000
            }}

mycollection.update_many(query,newvalues)

print(f' {result.modified_count} adet kayıt güncellendi. ')

for i in mycollection.find():
    print(i)


