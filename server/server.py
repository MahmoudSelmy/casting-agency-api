from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from database import ActorAccess, MovieAccess
from models import setup_db
from auth import requires_auth


class Server:
    def __init__(self, name):
        self.flask_server = Flask(name)
        CORS(self.flask_server)
        setup_db(self.flask_server)
        self._build_end_points()

    def _build_end_points(self):
        self._build_after_request()
        self._build_actors_end_points()
        self._build_movies_end_points()
        self._build_error_handlers()

    def _build_after_request(self):
        @self.flask_server.after_request
        def after_request(response):
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
            return response

    def _build_actors_end_points(self):
        self._build_get_actors_page_end_point()
        self._build_post_actor_end_point()
        self._build_patch_actor_end_point()
        self._build_delete_actor_end_point()

    def _build_get_actors_page_end_point(self):
        @self.flask_server.route('/actors', methods=['GET'])
        @requires_auth('get:actors')
        def get_actors():
            page_number = request.args.get('page', 1, type=int)
            actors = ActorAccess.get_actors_page(page_number)

            if len(actors) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'actors': actors,
                'total_actors': ActorAccess.get_total_number()
            })

    def _build_post_actor_end_point(self):
        @self.flask_server.route('/actors', methods=['POST'])
        @requires_auth('post:actors')
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

    def _build_patch_actor_end_point(self):
        @self.flask_server.route('/actors/<actor_id>', methods=['PATCH'])
        @requires_auth('patch:actors')
        def patch_actor(actor_id):
            body = request.get_json()

            if (actor_id is None) or (body is None):
                abort(400)

            try:
                actor = ActorAccess.update_actor(actor_id, body)
                return jsonify({
                    'success': True,
                    'actor_id': actor.id,
                    'actors': [actor.format()]
                })
            except Exception as e:
                print(e)
                abort(404)

    def _build_delete_actor_end_point(self):
        @self.flask_server.route('/actors/<actor_id>', methods=['DELETE'])
        @requires_auth('delete:actors')
        def delete_actors(actor_id):

            if actor_id is None:
                abort(400)

            try:
                ActorAccess.delete_actor(actor_id)
            except Exception as e:
                print(e)
                abort(404)

            return jsonify({
                'success': True,
                'actor_id': int(actor_id)
            })

    def _build_movies_end_points(self):
        self._build_get_movies_page_end_point()
        self._build_post_movie_end_point()
        self._build_patch_movie_end_point()
        self._build_delete_movie_end_point()

    def _build_get_movies_page_end_point(self):
        @self.flask_server.route('/movies', methods=['GET'])
        @requires_auth('get:movies')
        def get_movies():
            page_number = request.args.get('page', 1, type=int)
            movies = MovieAccess.get_movies_page(page_number)

            if len(movies) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'movies': movies,
                'total_movies': MovieAccess.get_total_number()
            })

    def _build_post_movie_end_point(self):
        @self.flask_server.route('/movies', methods=['POST'])
        @requires_auth('post:movies')
        def post_movie():
            body = request.get_json()
            if body is None:
                abort(400)
            try:
                movie = MovieAccess.create_movie(body)
                return jsonify({
                    'success': True,
                    'movie_id': movie.id
                })
            except Exception as e:
                print(e)
                abort(422)

    def _build_patch_movie_end_point(self):
        @self.flask_server.route('/movies/<movie_id>', methods=['PATCH'])
        @requires_auth('patch:movies')
        def patch_movie(movie_id):
            body = request.get_json()

            if (movie_id is None) or (body is None):
                abort(400)

            try:
                movie = MovieAccess.update_movie(movie_id, body)
                return jsonify({
                    'success': True,
                    'movie_id': movie.id,
                    'movies': [movie.format()]
                })
            except Exception as e:
                print(e)
                abort(404)

    def _build_delete_movie_end_point(self):
        @self.flask_server.route('/movies/<movie_id>', methods=['DELETE'])
        @requires_auth('delete:movies')
        def delete_movie(movie_id):

            if movie_id is None:
                abort(400)

            try:
                MovieAccess.delete_movie(movie_id)
            except Exception as e:
                print(e)
                abort(404)

            return jsonify({
                'success': True,
                'movie_id': int(movie_id)
            })

    def _build_error_handlers(self):
        @self.flask_server.errorhandler(422)
        def un_processable(error):
            return jsonify({
                "success": False,
                "error": 422,
                "message": "un-processable"
            }), 422

        @self.flask_server.errorhandler(401)
        def un_authorized(error):
            return jsonify({
                "success": False,
                "error": 401,
                "message": "un-authorized"
            }), 401

        @self.flask_server.errorhandler(403)
        def forbidden(error):
            return jsonify({
                "success": False,
                "error": 403,
                "message": "forbidden"
            }), 403

        @self.flask_server.errorhandler(400)
        def bad_request(error):
            return jsonify({
                "success": False,
                "error": 400,
                "message": "bad request"
            }), 400

        @self.flask_server.errorhandler(404)
        def not_found(error):
            return jsonify({
                "success": False,
                "error": 404,
                "message": "resource not found"
            }), 404

