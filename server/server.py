import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from database import ActorAccess


class Server:
    def __init__(self, name):
        self.flask_server = Flask(name)
        CORS(self.flask_server)
        self._build_end_points()

    def _build_end_points(self):
        self._build_actors_end_points()

    def _build_actors_end_points(self):
        self._build_get_actors_page_end_point()
        self._build_post_actor_end_point()

    def _build_get_actors_page_end_point(self):
        @self.flask_server.route('/actors', methods=['GET'])
        def get_actors():
            page_number = request.args.get('page', 1, type=int)
            actors = ActorAccess.get_actors_page(page_number)

            if len(page_number) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'actors': actors,
                'total_actors': ActorAccess.get_total_number()
            })

    def _build_post_actor_end_point(self):
        @self.flask_server.route('/actors', methods=['POST'])
        def post_actor():
            body = request.get_json()
            if body is None:
                abort(400)
            try:
                actor = ActorAccess.create_actor(body)
                return jsonify({
                    'success': True,
                    'actor_id': actor.id
                })
            except Exception as e:
                print(e)
                abort(422)
