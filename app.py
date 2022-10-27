# TODO 1. Host a server
# hosted jso data at https://kawalpreettkaur.github.io/hng/data.json

from flask import Flask, jsonify, request

app = Flask(__name__)

json_data = {

            "slackUsername": "kawalpreettkaur",
            "backend": True,
            "age": 27,
            'bio': "I am an Indian woman coder. And I am excited to be part of HNG team. Apart from coding, I like reading and chess. ",
    }


#retrieve the json data

# create an get endpoint that returns json response

@app.route('/jsonResponse')

def get_jsonData():
    
    return jsonify(json_data)


# if __name__ == '__main__':
app.run(debug=True)

# from http.server import BaseHTTPRequestHandler, HTTPServer
# import json

# HOST = "localhost"
# serverPort = 8000

# # json data

# _json_data = [
#     {
#         "slackUsername": "String",
#         "backend": "Boolean",
#         "age": 27,
#         'bio': 1593607500000,
#     }
# ]

# data =  json.dumps(_json_data)

# class WebServer(BaseHTTPRequestHandler):


#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'application/json')

#         self.end_headers()
#         self.wfile.write(data.encode('utf-8'))


# server = WebServer((HOST,serverPort),WebServer)
# print("Webserver is running now...")
# server.serve_forever()
# server.server_close()

# from http.server import BaseHTTPRequestHandler, HTTPServer
# from http import HTTPStatus
# import json
# import time

# hostName = "localhost"
# serverPort = 8000


# _g_posts = [
#     {
#         "slackUsername": "String",
#         "backend": "Boolean",
#         "age": 27,
#         'bio': 1593607500000,
#     }
# ]


# class MyServer(BaseHTTPRequestHandler):

#     def _set_headers(self):
#         self.send_response(HTTPStatus.OK.value)
#         self.send_header('Content-type', 'application/json')

#         self.end_headers()

#     def do_GET(self):
#         self._set_headers()
#         self.wfile.write(json.dumps(_g_posts).encode('utf-8'))


# if __name__ == "__main__":
#     webServer = HTTPServer((hostName, serverPort), MyServer)
#     print("Server started http://%s:%s" % (hostName, serverPort))

#     try:
#         webServer.serve_forever()
#     except KeyboardInterrupt:
#         pass

#     webServer.server_close()
#     print("Server stopped.")
