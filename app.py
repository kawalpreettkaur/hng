# TODO 1. Host a server


from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

json_data ={

            "slackUsername": "kawalpreettkaur",
            "backend": True,
            "age": 27,
            "bio": "I am an Indian woman coder.I am excited to be part of HNG team. Apart from coding, I like reading and chess. ",
    }


#retrieve the json data

# create an get endpoint that returns json response

@app.route('/jsonresponse')

def get_jsonData():
    
    return jsonify(json_data)



app.run(host='0.0.0.0', port=81)
