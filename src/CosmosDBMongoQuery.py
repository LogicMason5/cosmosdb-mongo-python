import pymongo
import CosmosDBMongoConnection as mc

# Connect to the Mongo or CosmosDB Mongo API instance
# from the environment variables and return the Collection
theCollection = mc.connectAndGetCollection()

# Query Database collection for item with comment field containing ....
mongoQueryString = { 'comment': 'Do nothing' }

result = theCollection.find(mongoQueryString)
print("Listing all documents where 'comment': 'Do nothing' matches")
for x in result:
    print(x)




