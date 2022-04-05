## Para maiores informeações, acesse: https://www.w3schools.com/python/python_mongodb_getstarted.asp

import pymongo

myclient = pymongo.MongoClient("mongodb://admin:123456@localhost:27017")

mydb = myclient["vendas"]

mycol = mydb["pessoas"]

mydoc = mycol.find().sort("nome")

for x in mydoc:
  print(x)