from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/returnjson', methods=['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {

            "slackUsername": "kawalpreettkaur",
            "backend": True,
            "age": 27,
            'bio': "I am an Indian woman coder. And I am excited to be part of HNG team. Apart from coding, I like reading and chess. ",
        }

        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
