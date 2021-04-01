import CosmosDBMongoConnection as mc

# Connect to the Mongo or CosmosDB Mongo API instance
# from the environment variables and return the Collection
theCollection = mc.connectAndGetCollection()

# Delete one document in the collection
theCollection.delete_many({'state':'MA'})

print("Deleted all documents where state is MA")

print("Listing all remaining documents. Check there is no document from the state of MA")

result = theCollection.find()

for x in result:
    print(x)

