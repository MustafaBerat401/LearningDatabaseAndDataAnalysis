import pymongo
from bson.objectid import ObjectId

#myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://mustafaberat:cKdwyV6BfT9XjDDp@cluster0.w72et.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]


# result = mycollection.find_one({"name":"Samsung S5"})
# result = mycollection.find_one({"_id": ObjectId("606bff746ba1d772afe3bf8f")})


# $in komutu bu isimde olan kayıtları bulur
# result = mycollection.find({
#     "name": {
#         "$in": ["Samsung S5","Samsung S6"] 
#     }
# })

# $gt (greaterthan) belirttiğimiz sayıdan büyük olan değerleri bulur 
# $gte (greaterthanequal) belirttiğimiz sayıdan büyük olan ve eşit olan değerleri bulur 
# result = mycollection.find({
#     "price":{
#         "$gt":2000
#     }
# })

# result = mycollection.find({
#     "price":{
#         "$gte":2000
#     }
# })

# $eq (equal) eşitlik operatörüdür 
# result = mycollection.find({
#     "price":{
#         "$eq":2000
#     }
# })

# $lt (lessthan) belirttiğimiz sayıdan küçük olan değerleri gösterir
# $lte (lessthanequal) belirttiğimiz sayıdan küçük olan ve eşit olan değerleri gösterir
result = mycollection.find({
    "price":{
        "$lt":2000
    }
})

# $regex (regularexpresion) istediğimiz herhangi bir kelimenin harfin ya da sayının hangi kayıtlar içerisinde varsa o kayıtları getirir.
result = mycollection.find({
    "name":{"$regex":"^S"}
})

for i in result:
    print(i)




