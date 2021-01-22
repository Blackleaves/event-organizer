from models.base_model import BaseModel
from app import db


class User(BaseModel):
    __tablename__ = 'users'

    nickname = db.Column(db.String(), default='noname')
    name = db.Column(db.String(), default='John Doe')
    email = db.Column(db.Unicode())
    description = db.Column(db.String())
    role = db.Column(db.Integer(), db.ForeignKey('roles.id'))

    def __str__(self):
        return f'{self.name} - {self.role}'
