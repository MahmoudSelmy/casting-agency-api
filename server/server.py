import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


class Server:
    def __init__(self, name):
        self.flask_server = Flask(name)
        CORS(self.flask_server)
        self._build_end_points()

    def _build_end_points(self):
        pass
