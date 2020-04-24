#cmd > pip install pymongo
import pymongo

# cONNECTING tO sERVER...
# ! rEPLACE sTRING "mongodb://localhost:27017/" wITH cLUSTER URL fOR cLOUD sTORAGE
client = pymongo.MongoClient("mongodb://localhost:27017/")

DB_list = client.list_database_names()

print(DB_list)