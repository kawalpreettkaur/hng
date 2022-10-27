# TODO 1. Host a server
# hosted jso data at https://kawalpreettkaur.github.io/hng/data.json

from flask import Flask, jsonify, request

app = Flask(__name__)

json_data = {

            "slackUsername": "kawalpreettkaur",
            "backend": True,
            "age": 27,
            'bio': "I am an Indian woman coder.I am excited to be part of HNG team. Apart from coding, I like reading and chess. ",
    }


#retrieve the json data

# create an get endpoint that returns json response

@app.route('/jsonResponse')

def get_jsonData():
    
    return jsonify(json_data)



app.run(debug=True)
