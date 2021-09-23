import pymongo


# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://mustafaberat:cKdwyV6BfT9XjDDp@cluster0.w72et.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find().sort('name',-1)
# result = mycollection.find().sort('price',-1)
result = mycollection.find().sort([('name',1), ('price',-1)])

for i in result:
    print(i)






