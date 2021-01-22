from models.base_model import BaseModel
from app import db


class Event(BaseModel):
    __tablename__ = 'events'

    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())
    creator_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __str__(self):
        return f'{self.title} - {self.description}'
