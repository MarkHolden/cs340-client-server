
from pymongo import MongoClient
from bson.objectid import ObjectId
from ArgumentException import ArgumentException

class AnimalShelterRepository(object):
    """CRUD operations for Animal Shelter."""

    def __init__(self, username: str, password: str):
        self.client = MongoClient("mongodb://%s:%s@localhost:27017/" % (username, password))
        self.db = self.client['AAC']

    # Create
    # A method that inserts a document into a specified MongoDB database and collection
    # Input -> argument to function will be set of key/value pairs in the data type acceptable to the MongoDB driver insert API call
    # Return -> "True" if successful insert, else "False"
    def create(self, data: dict):
        """Insert a new Animal record."""
        if data is None:
            raise ArgumentException(["Data"])
        else:
            result = self.db.animals.insert_one(data)
            return result.inserted_id is not None

    # Read
    # A method that gets a document by Id from a specified MongoDB database and specified collection
    # Input -> ObjectId use with the MongoDB driver find API call
    # Return -> result in cursor if successful, else MongoDB returned error message
    def get(self, _id: ObjectId):
        """Get an Animal record by ObjectId."""
        if _id is None:
            raise ArgumentException(["Id"])
        else:
            cursor = self.db.animals.find({ '_id': _id }).limit(1)
            for doc in cursor:
                return doc

    # Query
    # A method that queries for documents from a specified MongoDB database and specified collection
    # Input -> arguments to function should be the key/value lookup pair to use with the MongoDB driver find API call
    # Return -> result in cursor if successful, else MongoDB returned error message
    def query(self, query: dict, page: int = 1, page_size: int = 10):
        """Query for a matching Animal record."""
        if query is None:
            raise ArgumentException(["Query"])
        else:
            skip_count = page - 1 * page_size
            # Important: Be sure to use find() instead of find_one() when developing your method.
            if skip_count > 0:
                cursor = self.db.animals.find(query).skip(skip_count).limit(page_size)
            else:
                cursor = self.db.animals.find(query).limit(page_size)
            result = []
            for doc in cursor:
                result.append(doc)
            return result

    # Update
    # An Update method that queries for and changes document(s) from a specified MongoDB database and specified collection
    # Input -> arguments to function should be the key/value lookup pair to use with the MongoDB driver find API call.
    # Last argument to function will be a set of key/value pairs in the data type acceptable to the MongoDB driver insert API call.
    # Return -> result in JSON format if successful, else MongoDB returned error message.
    def update(self, _id: ObjectId, data: dict):
        """Update a matching Animal record."""
        if data is None or _id is None:
            null_args = []
            if data is None:
                null_args.append("Data")
            if _id is None:
                null_args.append("Id")
            raise ArgumentException(null_args)
        else:
            self.db.animals.update_one({ '_id': _id }, { "$set": data })

    # Delete
    # A Delete method that queries for and removes document(s) from a specified MongoDB database and specified collection
    # Input -> arguments to function should be the key/value lookup pair to use with the MongoDB driver find API call.
    # Return -> result in JSON format if successful, else MongoDB returned error message.
    def delete(self, _id: ObjectId):
        """Delete an Animal record."""
        if _id is None:
            raise ArgumentException(["Id"])
        else:
            delete_result = self.db.animals.delete_one({ '_id': _id })
            return delete_result.deleted_count > 0
