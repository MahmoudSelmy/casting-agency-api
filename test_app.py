import os
import unittest
import json
from server import Server
from utils.tokens import *
from datetime import date


class AgencyTestCase(unittest.TestCase):
    def setUp(self):
        server = Server(__name__)
        self.app = server.flask_server
        self.client = self.app.test_client
        self.new_actor = {
            'name': 'Selmy',
            'age': 26,
            'gender': 'Male'
        }
        self.new_movie = {
            'title': 'Movie',
            'release_date': '2016-03-25'
        }
        self.new_age = {
            'age': 18
        }
        self.new_release_date = {
            'release_date': '2024-03-25'
        }

    def test_post_actor_casting_assistant_returns_401(self):
        res = self.client().post('/actors', json=self.new_actor, headers=casting_assistant_auth_header)
        self.assertEqual(res.status_code, 401)

    def test_post_actor_executive_producer_returns_200(self):
        res = self.client().post('/actors', json=self.new_actor, headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['actor_id'] > 0)

    def test_post_actor_casting_director_returns_200(self):
        res = self.client().post('/actors', json=self.new_actor, headers=casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['actor_id'] > 0)

    def test_post_actor_missing_data_returns_422(self):
        new_actor = {
            'age': 26,
            'gender': 'Male'
        }
        res = self.client().post('/actors', json=new_actor, headers=casting_director_auth_header)
        self.assertEqual(res.status_code, 422)

    # ================================================

    def test_get_all_actors_valid_page_returns_200(self):
        res = self.client().get('/actors?page=1', headers=casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) > 0)

    def test_get_all_actors_invalid_page_returns_404(self):
        res = self.client().get('/actors?page=1000', headers=casting_assistant_auth_header)
        self.assertEqual(res.status_code, 404)

    def test_get_all_actors_without_auth_header_returns_401(self):
        res = self.client().get('/actors?page=1')
        self.assertEqual(res.status_code, 401)

    # ==================================================

    def test_patch_actor_executive_producer_returns_200(self):
        res = self.client().patch('/actors/2', json=self.new_age, headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['actors']), 1)
        self.assertEqual(data['actor_id'], 2)

    def test_patch_actor_casting_director_returns_200(self):
        res = self.client().patch('/actors/2', json=self.new_age, headers=casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['actors']), 1)
        self.assertEqual(data['actor_id'], 2)

    def test_patch_actor_casting_assistant_returns_401(self):
        res = self.client().patch('/actors/2', json=self.new_age, headers=casting_assistant_auth_header)
        self.assertEqual(res.status_code, 401)

    def test_patch_actor_invalid_id_returns_404(self):
        res = self.client().patch('/actors/20000', json=self.new_age, headers=casting_director_auth_header)
        self.assertEqual(res.status_code, 404)

    # ===================================================

    def test_delete_actor_executive_producer_returns_200(self):
        res = self.client().delete('/actors/1', headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor_id'], 1)

    def test_delete_actor_casting_director_returns_200(self):
        res = self.client().delete('/actors/2', headers=casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor_id'], 2)

    def test_delete_actor_casting_assistant_returns_401(self):
        res = self.client().delete('/actors/2', headers=casting_assistant_auth_header)
        self.assertEqual(res.status_code, 401)

    def test_delete_actor_invalid_id_returns_404(self):
        res = self.client().delete('/actors/1000', headers=casting_director_auth_header)
        self.assertEqual(res.status_code, 404)

    # ===================================================

    def test_post_movie_casting_assistant_returns_401(self):
        res = self.client().post('/movies', json=self.new_movie, headers=casting_assistant_auth_header)
        self.assertEqual(res.status_code, 401)

    def test_post_movie_casting_director_returns_401(self):
        res = self.client().post('/movies', json=self.new_movie, headers=casting_director_auth_header)
        self.assertEqual(res.status_code, 401)

    def test_post_movie_executive_producer_returns_200(self):
        res = self.client().post('/movies', json=self.new_movie, headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['movie_id'] > 0)

    def test_post_movie_missing_data_returns_422(self):
        new_movie = {
            'release_date': '2016-03-25'
        }
        res = self.client().post('/movies', json=new_movie, headers=executive_producer_auth_header)
        self.assertEqual(res.status_code, 422)

    # ================================================

    def test_get_all_movies_valid_page_returns_200(self):
        res = self.client().get('/movies?page=1', headers=casting_assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']) > 0)

    def test_get_all_movies_invalid_page_returns_404(self):
        res = self.client().get('/movies?page=1000', headers=casting_assistant_auth_header)
        self.assertEqual(res.status_code, 404)

    def test_get_all_movies_without_auth_header_returns_401(self):
        res = self.client().get('/movies?page=1')
        self.assertEqual(res.status_code, 401)

    # ==================================================

    def test_patch_movie_executive_producer_returns_200(self):
        res = self.client().patch('/movies/2', json=self.new_release_date, headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['movies']), 1)
        self.assertEqual(data['movie_id'], 2)

    def test_patch_movie_casting_director_returns_200(self):
        res = self.client().patch('/movies/2', json=self.new_release_date, headers=casting_director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['movies']), 1)
        self.assertEqual(data['movie_id'], 2)

    def test_patch_movie_casting_assistant_returns_401(self):
        res = self.client().patch('/movies/2', json=self.new_release_date, headers=casting_assistant_auth_header)
        self.assertEqual(res.status_code, 401)

    def test_patch_movie_invalid_id_returns_404(self):
        res = self.client().patch('/movies/20000', json=self.new_release_date, headers=casting_director_auth_header)
        self.assertEqual(res.status_code, 404)

    # ===================================================

    def test_delete_movie_executive_producer_returns_200(self):
        res = self.client().delete('/movies/2', headers=executive_producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movie_id'], 2)

    def test_delete_movie_casting_director_returns_401(self):
        res = self.client().delete('/movies/2', headers=casting_director_auth_header)
        self.assertEqual(res.status_code, 401)

    def test_delete_movie_casting_assistant_returns_401(self):
        res = self.client().delete('/movies/2', headers=casting_assistant_auth_header)
        self.assertEqual(res.status_code, 401)

    def test_delete_movie_invalid_id_returns_404(self):
        res = self.client().delete('/movies/1000', headers=executive_producer_auth_header)
        self.assertEqual(res.status_code, 404)

    # ===================================================


if __name__ == "__main__":
    unittest.main()
