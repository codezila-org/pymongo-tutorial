#cmd > pip install pymongo
import pymongo

# cONNECTING tO sERVER...
# ! rEPLACE sTRING "mongodb://localhost:27017/" wITH cLUSTER URL fOR cLOUD sTORAGE
client = pymongo.MongoClient("mongodb+srv://<yourusername>:<yourpassword>@cluster0-mgbud.mongodb.net/test?retryWrites=true&w=majority")

# cREATING dATABASE... 
db = client['grey-market']

# cREATING cOLLECTION...
usersCollection = db['Users']

data = { "name": "User Name", "email": "useremail@domain.com", "age": 20 }

# aDDING dATA tO cOLLECTION...
x = usersCollection.insert_one(data)

print(client.list_database_names())

