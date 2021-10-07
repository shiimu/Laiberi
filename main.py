from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
# Retrieves are imported for testing
    from accessDatabase import retrieveAvailable,retrieveBorrowed
    retrieveAvailable()
    retrieveBorrowed()
    return "Allooo"


if __name__ == "__main__":
    app.run( debug = True )