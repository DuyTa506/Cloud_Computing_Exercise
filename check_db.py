from pymongo import MongoClient

def read_mongodb_data(database_name, collection_name):
    client = MongoClient('mongodb://localhost:27017/')

    db = client[database_name]

    collection = db[collection_name]

    cursor = collection.find()

    for document in cursor:
        print(document)

    client.close()
read_mongodb_data('test', 'storage')
