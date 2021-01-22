from models.base_model import BaseModel
from app import db


class Perfomance(BaseModel):
    __tablename__ = 'perfomances'

    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())
    order = db.Column(db.Integer())
    duration = db.Column(db.Interval())
    person = db.Column(db.Integer(), db.ForeignKey('users.id'))
    stage = db.Column(db.Integer(), db.ForeignKey('stages.id'))

    def __str__(self):
        return f'{self.title} - {self.description} - Person {self.person} - Stage {self.stage}'
