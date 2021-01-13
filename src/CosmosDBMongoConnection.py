import pymongo
import os
import sys

#MONGO_URL = "mongodb://localhost:27017/"
#MONGO_URL = "mongodb://tbdemocosmosmongo:QPchq51HNg8RIuCyyX2sDwFKB4DOQYmom5U4vAlpTR1TtkdwGMuuIg97rRG3JINdX3lZgvi4g46uunxxHBs5rg==@tbdemocosmosmongo.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@tbdemocosmosmongo@"
#MONGO_DATABASE = "TBDocumentDB"
#MONGO_COLLECTION = "UserComments"

mongo_url = os.getenv("MONGO_URL")
mongo_database = os.getenv("MONGO_DATABASE", "")
mongo_collection = os.getenv("MONGO_COLLECTION", "")

def environment_variables_empty():
    # Verify if environment variables are empty
    if not mongo_url:
        sys.exit("MONGO_URL environment variable is not set. " +
                 "Please set environments MONGO_URL, MONGO_DATABASE, MONGO_COLLECTION and then try again.")
    if not mongo_database:
        sys.exit("MONGO_DATABASE environment variable is not set. " +
                 "Please set environments MONGO_URL, MONGO_DATABASE, MONGO_COLLECTION and then try again.")
    if not mongo_collection:
        sys.exit("MONGO_COLLECTION environment variable is not set. " +
                 "Please set environments MONGO_URL, MONGO_DATABASE, MONGO_COLLECTION and then try again.")
    return False

def connect():
    # Connect to the MongoDB/CosmosDB instance
    return pymongo.MongoClient(mongo_url)

def list_databases(aClient):
    # Display all the databases in the MongoDB/CosmosDB instance
    print(aClient.list_database_names())
    return

def is_database_present(aClient):
    # Check if the MONGO_DATABASE is present in the Server
    dbList = aClient.list_database_names()
    if mongo_database in dbList:
        print("The " + mongo_database + " database exists.")
        return True
    else:
        sys.exit("The " + mongo_database + " database DOS NOT exist. Create it first.")

def get_database(aClient):
    # Get the database
    return aClient[mongo_database]

def is_collection_present(aDB):
    # Check if the MONGO_COLLECTION exists
    if mongo_collection in aDB.list_collection_names():
        print("The " + mongo_collection + " collection exists.")
        return True
    else:
        sys.exit("The " +  mongo_collection + " collection DOES NOT exist in " + mongo_database + " database. Create it first.")

def get_collection(aDB):
    # Get the collection    
    return aDB[mongo_collection]

# Read environment variables, connect to server, database and return the collection
def connectAndGetCollection():
    # Get the connection urls from environment variables
    # and check if any are empty. Program quits if empty
    environment_variables_empty()

    # Connect to the server
    theClient = connect()
    # Print list of databases
    list_databases(theClient)
    # Check if the MONGO_DB database (from env variable)
    # exists. If not, the program quits
    is_database_present(theClient)
    # Get the handle to the database
    theDatabase = get_database(theClient)
    # Check if the collection exists in the database, if not quit
    is_collection_present(theDatabase)
    # Get the handle to the collection
    theCollection = get_collection(theDatabase)
    return theCollection
    
   
