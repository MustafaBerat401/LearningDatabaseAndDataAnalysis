import pymongo


# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://mustafaberat:cKdwyV6BfT9XjDDp@cluster0.w72et.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find_one()
for i in mycollection.find({},{"_id":0,"name":1}):
    print(i)







# print(result)   




