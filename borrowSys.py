# Function for stating the name of the book
def bookName(name):
    name = "baabab"
# Function for borrowing a book
# Importing from accessDatabase to add and remove books
def borrowBook():
    from accessDatabase import addBorrow, removeAvail
# Add to borrowed
    addBorrow()
# Delete from available
    removeAvail()
    
# Function for borrowing a book
# Importing from accessDatabase to add and remove books
def returnBook():
    from accessDatabase import addAvail, removeBorrow
# Add to available
    addAvail()
# Delete from borrowed
    removeBorrow()

