import CosmosDBMongoConnection as mc


def delete_documents_by_state(collection, state: str):
    """
    Delete all documents that match the given state.
    """
    result = collection.delete_many({"state": state})
    print(f"Deleted {result.deleted_count} document(s) where state = '{state}'")


def list_remaining_documents(collection):
    """
    List all documents currently in the collection.
    """
    print("\nListing remaining documents:")
    cursor = collection.find()

    for document in cursor:
        print(document)


def main():
    try:
        # Connect to MongoDB / CosmosDB collection
        collection = mc.connectAndGetCollection()

        # Delete documents where state = 'MA'
        delete_documents_by_state(collection, "MA")

        print("\nVerifying remaining documents (should contain no 'MA'):")

        # Display remaining documents
        list_remaining_documents(collection)

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
