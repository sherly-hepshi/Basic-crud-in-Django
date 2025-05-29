from pymongo import MongoClient
client=MongoClient("mongodb+srv://hepshiba:paulsherly@project.ngmzcan.mongodb.net/")
db=client["data"]
col=db["users"]