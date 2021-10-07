from pymongo import MongoClient,ALL

#COULD REDUCE THIS WITHOUT THE REPETITION!!!

# Retrieve available books from the database
def retrieveAvailable():
    client = MongoClient('localhost', 27017)
    db = client['Libari']
    collection = db['booksAvail']
    retrieved = list(collection.find({}, {'_id' : False}))
    print(retrieved)

# Retrieve borrowed books from the database
def retrieveBorrowed():
    client = MongoClient('localhost', 27017)
    db = client['Libari']
    collection = db['booksBorrow']
    retrieved = list(collection.find({}, {'_id' : False}))
    print(retrieved)

# Add to available books database
def addAvail():
    client = MongoClient('localhost', 27017)
    db = client['Libari']
    collection = db['booksAvail']
    collection.insert("Bookname")
# Add to borrowed books database
def addBorrow():
    client = MongoClient('localhost', 27017)
    db = client['Libari']
    collection = db['booksBorrow']
    collection.insert("Bookname")

# Remove from available database
def removeAvail():
    pass

# Remove from borrowed database
def removeBorrow():
    pass