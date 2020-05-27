from database import ActorAccess, MovieAccess


def mock_init_actors_data():
    for i in range(30):
        new_actor = {
            'name': 'Actor %s' % i,
            'age': 20 + i,
            'gender': 'Male' if i % 2 == 0 else 'Female'
        }
        ActorAccess.create_actor(new_actor)


def mock_init_movies_data():
    for i in range(30):
        new_movie = {
            'title': 'Movie %s' % i,
            'release_date': '2016-03-25'
        }
        MovieAccess.create_movie(new_movie)


def mock_init_data():
    mock_init_actors_data()
    mock_init_movies_data()
