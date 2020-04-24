#cmd > pip install pymongo
import pymongo

# cONNECTING tO sERVER...
# ! rEPLACE sTRING "mongodb://localhost:27017/" wITH cLUSTER URL fOR cLOUD sTORAGE
client = pymongo.MongoClient("mongodb://localhost:27017/")

# You Can use client for Database operations.