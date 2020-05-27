from models import Movie
from utils import paginate_items


class MovieAccess:
    @classmethod
    def get_all_movies(cls):
        movies = Movie.query.all()
        return movies

    @classmethod
    def get_movies_page(cls, page_number):
        movies = cls.get_all_movies()
        movies = paginate_items(page_number, movies)
        movies = [movie.format() for movie in movies]
        return movies

    @classmethod
    def get_total_number(cls):
        movies = cls.get_all_movies()
        return len(movies)

    @classmethod
    def _get_attribute_from_data(cls, data, attribute_name):
        attribute = data.get(attribute_name, None)
        if attribute is None:
            raise ValueError(attribute_name + ' must be provided')
        return attribute

    @classmethod
    def _convert_data_to_movie(cls, data):
        title = cls._get_attribute_from_data(data, 'title')
        release_date = cls._get_attribute_from_data(data, 'release_date')
        movie = Movie(title, release_date)
        return movie

    @classmethod
    def create_movie(cls, data):
        try:
            movie = cls._convert_data_to_movie(data)
            movie.insert()
        except Exception as e:
            raise ValueError(str(e))
        return movie

    @classmethod
    def get_movie_by_id(cls, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            raise ValueError('Invalid Movie_id')
        return movie

    @classmethod
    def update_movie(cls, movie_id, data):
        movie = cls.get_movie_by_id(movie_id)

        title = data.get('title', movie.title)
        release_date = data.get('release_date', movie.release_date)

        movie.title = title
        movie.release_date = release_date

        movie.update()

        return movie

    @classmethod
    def delete_movie(cls, movie_id):
        movie = cls.get_movie_by_id(movie_id)
        movie.delete()
