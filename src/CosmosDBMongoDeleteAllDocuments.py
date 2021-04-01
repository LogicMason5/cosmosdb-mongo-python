import CosmosDBMongoConnection as mc

# Connect to the Mongo or CosmosDB Mongo API instance
# from the environment variables and return the Collection
theCollection = mc.connectAndGetCollection()

# Delete all documents in the collection
theCollection.delete_many({})

print("Deleted all documents in the collection")

print("Listing all remaining documents. Check there is no documents displayed below")

result = theCollection.find()

for x in result:
    print(x)

