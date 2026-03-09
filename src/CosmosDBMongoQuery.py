import CosmosDBMongoConnection as mc


def find_documents_by_comment(collection, comment_text: str):
    """
    Find documents where the comment field matches the given text.
    """
    query = {"comment": comment_text}
    results = collection.find(query)

    documents = list(results)

    print(f"\nListing documents where comment = '{comment_text}'")
    print(f"Total documents found: {len(documents)}\n")

    for doc in documents:
        print(doc)


def main():
    try:
        # Connect to MongoDB / CosmosDB collection
        collection = mc.connectAndGetCollection()

        # Query documents
        find_documents_by_comment(collection, "Do nothing")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
