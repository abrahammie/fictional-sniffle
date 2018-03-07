# import socket

# HOST, PORT = '', 1981

# listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# listen_socket.bind((HOST, PORT))
# listen_socket.listen(1)
# print 'Listening on PORT %s ...' % PORT
# while True:
#   client_connection, client_address = listen_socket.accept()
#   request = client_connection.recv(1024)
#   print request

#   http_response = """\
# HTTP/1.1 200 OK

# Hello, World!
# """
#   client_connection.sendall(http_response)
#   client_connection.close()


from flask import Flask, render_template

app = Flask(__name__, static_folder="../client/dist", template_folder="../client")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == "__main__":
  app.run()