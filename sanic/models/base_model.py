from datetime import datetime
from app import db


class BaseModel(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    last_modified = db.Column(db.DateTime())
