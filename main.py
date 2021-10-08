from flask import Flask, render_template

from accessDatabase import removeAvail

app = Flask(__name__)


@app.route("/")
def index():
# Retrieves are imported for testing
    from accessDatabase import retrieveAvailable,retrieveBorrowed
    retrieveAvailable()
    retrieveBorrowed()
    return "Allooo"

@app.route("/borrow")
def borrow():
    from borrowSys import borrowBook
    borrowBook()
    return "Borrowed"

if __name__ == "__main__":
    app.run( debug = True )