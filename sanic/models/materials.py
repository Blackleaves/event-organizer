from models.base_model import BaseModel
from app import db


class Material(BaseModel):
    __tablename__ = 'materials'

    title = db.Column(db.String())
    description = db.Column(db.String())
    storage_url = db.Column(db.Unicode())
    perfomance = db.Column(db.Integer(), db.ForeignKey('perfomances.id'))

    def __str__(self):
        return f'{self.title} - {self.description}'
