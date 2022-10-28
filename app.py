from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread

# create a flask app
app = Flask(__name__)

# disabling jsonifier's auto sorting
app.config['JSON_SORT_KEYS'] = False

# enable CORS
# checked here: https://cors-test.codehappy.dev/?url=https%3A%2F%2Fjsonresponser.kawalpreetpreet.repl.co%2Fjsonresponse&method=get
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# json data to retrieve
json_data ={ 
  "slackUsername": "kawalpreettkaur", "backend": True, "age": 27, "bio": "I am an Indian woman coder.I am excited to be part of HNG team. Apart from coding, I like reading and chess." 
}
    
# retrieve the json data

# create an get endpoint that returns json response

@app.route('/jsonresponse')

def get_jsonData():
    
    return jsonify(json_data)

# replit stay awake
def index():
    return "<h1>Jsonifier is running!</h1>"

# app.run(host='0.0.0.0', port=81)
Thread(target=app.run,args=('0.0.0.0',8080)).start()


