import CosmosDBMongoConnection as mc

# Connect to the Mongo or CosmosDB Mongo API instance
# from the environment variables and return the Collection
theCollection = mc.connectAndGetCollection()

listOfComments = mylist = [
  { "name": "Amy", "address": "Apple st 652", "state": "MA", "comment": "Let us do something for nothing" },
  { "name": "Hannah", "address": "Mountain 21", "state": "GA", "comment": "Let us do nothing for something" },
  { "name": "Michael", "address": "Valley 345", "state": "NH", "comment": "Let us do something" },
  { "name": "Sandy", "address": "Ocean blvd 2", "state": "LA", "comment": "Let us do nothing" },
  { "name": "Betty", "address": "Green Grass 1", "state": "CA", "comment": "Do nothing" },
  { "name": "Richard", "address": "Sky st 331", "state": "IL", "comment": "No comments" },
  { "name": "Susan", "address": "One way 98", "state": "NY", "comment": "Cannot comment now" },
  { "name": "Vicky", "address": "Yellow Garden 2", "state": "AK", "comment": "Why comment?" },
  { "name": "Ben", "address": "Park Lane 38", "state": "FL", "comment": "Life is beautiful" },
  { "name": "William", "address": "Central st 954", "state": "NC", "comment": "Who is there?" },
  { "name": "Chuck", "address": "Main Road 989", "state": "TX", "comment": "I am fine" },
  { "name": "Viola", "address": "Sideway 1633", "state": "AZ", "comment": "Let us do something for nothing" }
]

result = theCollection.insert_many(listOfComments)

print(result.inserted_ids)

