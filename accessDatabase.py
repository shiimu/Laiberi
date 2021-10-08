from pymongo import MongoClient,ALL

# COULD REDUCE THIS WITHOUT THE REPETITION!!!
# ADD A STRING VARIABLE TO COLLECTION.FIND({VARIABLE_HERE}) SO IT CAN HELP WITH SEARCHING THE RIGHT BOOK
#"Name": "Web security for developers"
inputReturn = '"Web security for developers"'
# Function to find a book by a name
def findByName():
    name = '"Name"'
    # bookHeading should be a returned input.
    bookHeading = inputReturn
    global nameSearch
    nameSearch = name + ' : ' + bookHeading
    print(nameSearch)
    # nameSearch returns an error ATM! must fix!!
# Retrieve available books from the database
def retrieveAvailable():
    client = MongoClient('localhost', 27017)
    db = client['Libari']
    collection = db['booksAvail']
    retrieved = list(collection.find({nameSearch}, {'_id' : False}))
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
    collection.insert(bookName(name))
# Add to borrowed books database
def addBorrow():
    from borrowSys import bookName
    client = MongoClient('localhost', 27017)
    db = client['Libari']
    collection = db['booksBorrow']
    collection.insert(bookName(name))

# Remove from available database
def removeAvail():
    pass

# Remove from borrowed database
def removeBorrow():
    pass