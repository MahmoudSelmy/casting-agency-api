from server import Server


server = Server(__name__)
app = server.flask_server

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=8080, debug=True)
