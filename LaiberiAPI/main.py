from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from pymongo import ALL, MongoClient

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():

    return "Allooo"

# Class for interacting with available books collection
class Available(Resource):
    def get(self):
        client = MongoClient('localhost', 27017)
        db = client['Libari']
        collection = db['booksAvail']
        # had to make id not show, because it threw a not json serializable error.
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200

    def post(self):
        # Require these args for the POST request.
        parser = reqparse.RequestParser()
        parser.add_argument('name', required = True)
        parser.add_argument('writer', required = True)
        parser.add_argument('year', required = True)
        parser.add_argument('isbn', required = True)
        parser.add_argument('rating', required = True)
        parser.add_argument('about', required = True)
        parser.add_argument('tags', required = True)
        parser.add_argument('description', required = True)

        args = parser.parse_args()

        client = MongoClient('localhost', 27017)
        db = client['Libari']
        collection = db['booksAvail']
        new_book = collection.insert_one({
            'Name' : args['name'],
            'Writer' : args['writer'],
            'Year' : args['year'],
            'ISBN' : args['isbn'],
            'Rating' : args['rating'],
            'About' : args['about'],
            'Tags' : args['tags'],            
            'Description' : args['description']        
        })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
    
    def put(self):
        return 401

    def delete(self):
    # Require these args for the DELETE request.

        parser = reqparse.RequestParser()
        parser.add_argument('name', required = True)
        parser.add_argument('writer', required = True)
        parser.add_argument('year', required = True)
        parser.add_argument('isbn', required = True)
        parser.add_argument('rating', required = True)
        parser.add_argument('about', required = True)
        parser.add_argument('tags', required = True)
        parser.add_argument('description', required = True)
        args = parser.parse_args()

        client = MongoClient('localhost', 27017)
        db = client['Libari']
        collection = db['booksAvail']
        removeBook = collection.find_one_and_delete({
            'Name' : args['name'],
            'Writer' : args['writer'],
            'Year' : args['year'],
            'ISBN' : args['isbn'],
            'Rating' : args['rating'],
            'About' : args['about'],
            'Description' : args['description']        
        })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
        

    def push(self):
        return 401
# Class for interacting with borrowed books collection
class Borrowed(Resource):
    def get(self):
        client = MongoClient('localhost', 27017)
        db = client['Libari']
        collection = db['booksBorrow']
        # had to make id not show, because it threw a not json serializable error.
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200

    def post(self):
    # Require these args for the POST request.

        parser = reqparse.RequestParser()
        parser.add_argument('name', required = True)
        parser.add_argument('writer', required = True)
        parser.add_argument('year', required = True)
        parser.add_argument('isbn', required = True)
        parser.add_argument('rating', required = True)
        parser.add_argument('about', required = True)
        parser.add_argument('tags', required = True)
        parser.add_argument('description', required = True)

        args = parser.parse_args()

        client = MongoClient('localhost', 27017)
        db = client['Libari']
        collection = db['booksBorrow']
        new_book = collection.insert_one({
            'Name' : args['name'],
            'Writer' : args['writer'],
            'Year' : args['year'],
            'ISBN' : args['isbn'],
            'Rating' : args['rating'],
            'About' : args['about'],
            'Tags' : args['tags'],            
            'Description' : args['description']        
        })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
    
    def put(self):
        return 401

    def delete(self):
       # Require these args for the DELETE request.

        parser = reqparse.RequestParser()
        parser.add_argument('name', required = True)
        parser.add_argument('writer', required = True)
        parser.add_argument('year', required = True)
        parser.add_argument('isbn', required = True)
        parser.add_argument('rating', required = True)
        parser.add_argument('about', required = True)
        parser.add_argument('tags', required = True)
        parser.add_argument('description', required = True)
        args = parser.parse_args()

        client = MongoClient('localhost', 27017)
        db = client['Libari']
        collection = db['booksBorrow']
        removeBook = collection.find_one_and_delete({
            'Name' : args['name'],
            'Writer' : args['writer'],
            'Year' : args['year'],
            'ISBN' : args['isbn'],
            'Rating' : args['rating'],
            'About' : args['about'],
            'Description' : args['description']        
        })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
        

    def push(self):
        return 401

api.add_resource(Available, '/available')
api.add_resource(Borrowed, '/borrowed')


if __name__ == "__main__":
    app.run( debug = True )