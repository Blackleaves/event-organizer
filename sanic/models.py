from datetime import datetime
from app import db


class BaseModel(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    last_modified = db.Column(db.DateTime())


class Role(BaseModel):
    __tablename__ = 'roles'

    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())

    def __str__(self):
        return f'{self.title} - {self.description}'


class User(BaseModel):
    __tablename__ = 'users'

    nickname = db.Column(db.String(), default='noname')
    name = db.Column(db.String(), default='John Doe')
    email = db.Column(db.Unicode())
    description = db.Column(db.String())
    role = db.Column(db.Integer(), db.ForeignKey('roles.id'))

    def __str__(self):
        return f'{self.name} - {self.role}'


class Event(BaseModel):
    __tablename__ = 'events'

    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())
    creator_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __str__(self):
        return f'{self.title} - {self.description}'


class Stage(BaseModel):
    __tablename__ = 'stages'

    title = db.Column(db.String())
    description = db.Column(db.String())
    event_id = db.Column(db.Integer(), db.ForeignKey('events.id'))
    responsible = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __str__(self):
        return f'{self.title} - {self.description} - Event {self.event_id}'


class Performance(BaseModel):
    __tablename__ = 'performances'

    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())
    order = db.Column(db.Integer())
    duration = db.Column(db.Interval())
    person = db.Column(db.Integer(), db.ForeignKey('users.id'))
    stage = db.Column(db.Integer(), db.ForeignKey('stages.id'))

    def __str__(self):
        return f'{self.title} - {self.description} - Person {self.person} - Stage {self.stage}'


class Material(BaseModel):
    __tablename__ = 'materials'

    title = db.Column(db.String())
    description = db.Column(db.String())
    storage_url = db.Column(db.Unicode())
    performance = db.Column(db.Integer(), db.ForeignKey('performances.id'))

    def __str__(self):
        return f'{self.title} - {self.description}'
