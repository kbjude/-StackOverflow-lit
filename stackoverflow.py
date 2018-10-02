from flask import Flask
from Flask_restful import Api, Resources, reqparse
app = Flask(__name__)
app = Api(app)
users = [
    {
        "name": "Jude",
        "age": 45,
        "occupation": "information tech"
    },
    {
        "name": "Lillian",
        "age": 20,
        "occupation": "Counselor"        
    },
    {
        "name": "Isaiah",
        "age": 100,
        "occupation": "Proffessor"
    }


]

class User(Resource):
    def get(self, name):
        for user in user:
            if (name == user["name"]):
                return user, 200
            return "user not found", 400