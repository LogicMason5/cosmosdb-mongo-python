# cosmosdb-mongo-python

The python code here can be used to create, read, delete documents in MongoDB or in CosmosDB running MongoDB model. With NO CODE CHANGE, you can run these on MongDB and CosmosDB. This makes it easy to migrate your application from a MongoDB IaaS instance to a managed, globally distributed, scalable cloud based CosmosDB.

You just need to pass the URL to connect to MongoDB or CosmosDB, the name of your Database and Collection as environment variables to run the code.

This is possible due to wire protocol compatibility implemented by Azure CosmosDB for MongoDB. This allows transparent compatibility with native MongoDB client SDKs, drivers and tools. Azure CosmosDB does not host the MongoDB database engine. More details are in the [CosmosDB documentation page][azure-cosmosdb-docs]

## Prerequisites ##

You should have an instance of MongoDB running, ONLY if you want to test the python code against a MongoDB instance. Check out - [Install MongoDB in Windows][mongodb-installation]. Note the MongoDB URL (e.g. mongodb://localhost:27017/) 

You should have an instance of CosmosDB running, ONLY if you want to test the python code against a CosmosDB instance. Check out - [Install CosmosDB for MongoDB API in Azure][cosmosdb-mongoapi-installation]. Note the CosmosDB URL. You can find it from the Azure Portal, in your left side "Connection String" menu bar for the CosmosDB instance.
![CosmosDB URL](/images/logo.png)
Format: ![Alt Text](CosmosDB URL)

On the client 

[azure-cosmosdb-docs]: <https://docs.microsoft.com/en-us/azure/cosmos-db/mongodb-introduction>
[mongodb-installation]: <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/>
[cosmosdb-mongoapi-installation]: <https://docs.microsoft.com/en-us/azure/cosmos-db/create-mongodb-flask#create-a-database-account>
