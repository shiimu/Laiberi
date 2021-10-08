from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from pymongo import ALL, MongoClient

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():

    return "Allooo"


class Name(Resource):
    def get(self):
        client = MongoClient('localhost', 27017)
        db = client['Libari']
        collection = db['booksAvail']
        # had to make id not show, because it threw a not json serializable error.
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200

    def post(self):
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
            'Description' : args['description']        
        })    
        retrieved = list(collection.find({}, {'_id' : False}))
        return retrieved, 200
    
    def put(self):
        return 401

    def delete(self):
# WORK ON THIS!!! DELETE THE WHOLE DOCUMENT NOT SOME STRINGS
        parser = reqparse.RequestParser()
        args = parser.parse_args()

        client = MongoClient('localhost', 27017)
        db = client['Libari']
        collection = db['booksAvail']
        removeBook = collection.delete_one({
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

api.add_resource(Name, '/name')


if __name__ == "__main__":
    app.run( debug = True )