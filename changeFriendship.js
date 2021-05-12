// start transaction
var session = db.getMongo().startSession();
var userCommentsCollection = session.getDatabase("TBDocumentDB").UserComments;
session.startTransaction();
// operations in transaction
try {
	userCommentsCollection.updateOne({ name: "Amy" }, { $set: { friendOf: "Michael" } } );
	userCommentsCollection.updateOne({ name: "Hannah" }, { $set: { friendOf: "Michael" } } );
} catch (error) {
	// abort transaction on error
	session.abortTransaction();
	throw error;
}

// commit transaction
session.commitTransaction();