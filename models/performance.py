from .core import db

Performance = db.Table('Performance', db.Model.metadata,
                       db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')),
                       db.Column('actor_id', db.Integer, db.ForeignKey('actors.id')),
                       )
