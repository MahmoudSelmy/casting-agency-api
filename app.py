from server import Server


app = Server(__name__)

if __name__ == '__main__':
    app.flask_server.run(host='0.0.0.0', port=8080, debug=True)
