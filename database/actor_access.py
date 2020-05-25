from models import Actor
from utils import paginate_items


class ActorAccess:
    @classmethod
    def get_all_actors(cls):
        actors = Actor.query.all()
        return actors

    @classmethod
    def get_actors_page(cls, page_number):
        actors = cls.get_all_actors()
        actors = paginate_items(page_number, actors)
        actors = [actor.format() for actor in actors]
        return actors

    @classmethod
    def get_total_number(cls):
        actors = cls.get_all_actors()
        return len(actors)
