from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from database import ActorAccess, MovieAccess


class Server:
    def __init__(self, name):
        self.flask_server = Flask(name)
        CORS(self.flask_server)
        self._build_end_points()

    def _build_end_points(self):
        self._build_actors_end_points()
        self._build_movies_end_points()

    def _build_actors_end_points(self):
        self._build_get_actors_page_end_point()
        self._build_post_actor_end_point()
        self._build_patch_actor_end_point()
        self._build_delete_actor_end_point()

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

    def _build_patch_actor_end_point(self):
        @self.flask_server.route('/actors/<actor_id>', methods=['PATCH'])
        def patch_actor(actor_id):
            body = request.get_json()

            if (actor_id is None) or (body is None):
                abort(400)

            try:
                actor = ActorAccess.update_actor(actor_id, body)
                return jsonify({
                    'success': True,
                    'actor_id': actor_id,
                    'actors': [actor.format()]
                })
            except Exception as e:
                print(e)
                abort(404)

    def _build_delete_actor_end_point(self):
        @self.flask_server.route('/actors/<actor_id>', methods=['DELETE'])
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
                'actor_id': actor_id
            })

    def _build_movies_end_points(self):
        self._build_get_movies_page_end_point()
        self._build_post_movie_end_point()
        self._build_patch_movie_end_point()

    def _build_get_movies_page_end_point(self):
        @self.flask_server.route('/movies', methods=['GET'])
        def get_movies():
            page_number = request.args.get('page', 1, type=int)
            movies = MovieAccess.get_movies_page(page_number)

            if len(page_number) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'movies': movies,
                'total_movies': MovieAccess.get_total_number()
            })

    def _build_post_movie_end_point(self):
        @self.flask_server.route('/movies', methods=['POST'])
        def post_actor():
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
        def patch_actor(movie_id):
            body = request.get_json()

            if (movie_id is None) or (body is None):
                abort(400)

            try:
                movie = MovieAccess.update_movie(movie_id, body)
                return jsonify({
                    'success': True,
                    'actor_id': movie_id,
                    'actors': [movie.format()]
                })
            except Exception as e:
                print(e)
                abort(404)
