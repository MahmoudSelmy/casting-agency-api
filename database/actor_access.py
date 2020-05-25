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

    @classmethod
    def _get_attribute_from_data(cls, data, attribute_name):
        attribute = data.get(attribute_name, None)
        if attribute is None:
            raise ValueError(attribute_name + ' must be provided')
        return attribute

    @classmethod
    def _convert_data_to_actor(cls, data):
        name = cls._get_attribute_from_data(data, 'name')
        age = cls._get_attribute_from_data(data, 'age')
        gender = cls._get_attribute_from_data(data, 'gender')
        actor = Actor(name, gender, age)
        return actor

    @classmethod
    def create_actor(cls, data):
        try:
            actor = cls._convert_data_to_actor(data)
            actor.insert()
        except Exception as e:
            raise ValueError(str(e))
        return actor
