from flask import Flask
from flask import request, jsonify 

app = Flask(__name__)

@app.route('/')
def home():
    data = {"message":"Welcome to stackoverflow lite"}
    return "<h1> Hello World </h1>"
    return jsonify(data)
@app.route('/summary')
def summary():
    d = {"message":"Coming soon"}
    return jsonify(d)
@app.route('/login', methods = ['POST'])
def login():
    message = "Logged in successfully"
    data = request.get_json()
    if "username" not in data.keys():
        message = "Please provide a user name"
    response = {"message":message}
    return jsonify(response), 404

if __name__ =="__main__":
    app.run(debug=True,port=8080)