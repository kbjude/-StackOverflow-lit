""" Importing the flask module"""
import uuid
from flask import Flask
from flask import request, jsonify

APP = Flask(__name__)

QUESTIONS = []
ANSWERS = []
USERS = []

@APP.route('/')
def index():
    """First display page"""
    return "<h1>CHALLENGE 2</h1>"

@APP.route('/questions', methods=['POST'])
def send_question():
    '''Handle a question'''
    #Convert the request parameters into dictionary
    data = request.get_json()
    status_code = 200
    message = "Question created successfuly"
    #Validate inputs
    if "content" not in data.keys():
        message = "Provide a question"
        status_code = 400

    if "category" not in data.keys():
        message = "Provide the right category"
        status_code = 400

    if status_code == 200:
        data["id"] = str(uuid.uuid1())
        QUESTIONS.append(data)

    output = {"message":message}

    if  "id" in data.keys():
        output["id"] = data["id"]

    return jsonify(output), status_code

@APP.route('/answers', methods=['POST'])
def question_answer():
    '''Endpoint for creating answer'''
    answer = request.get_json()
    status_code = 200
    message = "Answer submitted successfuly"

    if "question_id" not in answer.keys():
        message = "You have not selected any question"
        status_code = 400
    else:
        status_code = 400
        for question in QUESTIONS:
            if question["id"] == answer["question_id"]:
                status_code = 200
                break
        if status_code == 400:
            message = "Question does not exisit"

    if "answer" not in answer.keys():
        message = "You have not typed any thing in you answer, do you want to submit ablank form?"
        status_code = 400

    if status_code == 200:
        answer["id"] = str(uuid.uuid1())
        ANSWERS.append(answer)

    output = {"message":message}

    if  "id" in answer.keys():
        output["id"] = answer["id"]

    return jsonify(output), status_code

@APP.route('/signup', methods=['POST'])
def signup():
    """ signup endpoint """
    data = request.get_json()
    status_code = 200
    message = "User registered successfully"

    if "username" not in data.keys():
        status_code = 400
        message = "You have an empty input"

    else:
        #This is a username from json
        if "username" in data.keys():
            #loops thru the List
            for user in USERS:
                if user["username"] == data["username"]:
                    status_code = 400
                    message = "Username already exists"
                    break

        if "confirm" not in data.keys():
            status_code = 400
            message = "Variable confirm is no where to be seen"

        if "password" not in data.keys():
            status_code = 400
            message = "Variable password is no where to be seen"
# work on this as soon as i reach office
        if len("password") == len("confirm"):
            status_code = 200
            message = "Username and password successfully saved"
        else:
            len("password") != len("confirm")

    #if status_code == 400:
     #   message = "The user you are trying to create already exists"

    if status_code == 200:
        USERS.append(data)

    output = {"message":message}

    return jsonify(output), status_code

@APP.route('/signin', methods=['POST'])
def signin():
    """ The signin endpoint """
    data = request.get_json()
    status_code = 200
    message = "Logged in succesfuly"
#work on first thing in office
    if "username" not in data.keys():
        status_code = 400
        message = "No username"
    else:
        for user in USERS:
            if user["username"] not in data["username"]:
                status_code = 400
                message = "User does not exist"

    #if status_code == 200:
        output = {"message": message}
        return jsonify(output), status_code
"""
@APP.route('/receive_questions', methods = ['GET'])
def receive_questions():
    result = "result"
    return jsonify({"key":['1','2']})
@APP.route('/receive_question', methods = ['GET'])
def receive_question():
    single_result = "single_result"
    return jsonify(single_result) 

"""
if __name__ =="__main__":
    APP.run(debug=True)
