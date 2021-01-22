from models.base_model import BaseModel
from app import db


class Role(BaseModel):
    __tablename__ = 'roles'

    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())

    def __str__(self):
        return f'{self.title} - {self.description}'
