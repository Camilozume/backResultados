import pymongo
import certifi


ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://camilozume:P4$$w0rd@proyregistraduria.zzkkhpn.mongodb.net/registraduria_db?retryWrites=true&w=majority",
    tlsCAFile=ca
)
db = client.test
print(db)

data_base = client['registraduria_db']
print(data_base.list_collection_names())
