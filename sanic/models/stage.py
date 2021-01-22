from models.base_model import BaseModel
from app import db


class Stage(BaseModel):
    __tablename__ = 'stages'

    title = db.Column(db.String())
    description = db.Column(db.String())
    event_id = db.Column(db.Integer(), db.ForeignKey('events.id'))
    responsible = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __str__(self):
        return f'{self.title} - {self.description} - Event {self.event_id}'
