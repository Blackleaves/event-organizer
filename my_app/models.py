from datetime import datetime

from app import db


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    last_modified = db.Column(db.DateTime())
    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())

    def __str__(self):
        return f'{self.title} - {self.description}'


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    last_modified = db.Column(db.DateTime())
    nickname = db.Column(db.String(), default='noname')
    name = db.Column(db.String(), default='John Doe')
    email = db.Column(db.Unicode())
    description = db.Column(db.String())
    role = db.Column(db.Integer(), db.ForeignKey('roles.id'))

    def __str__(self):
        return f'{self.name} - {self.role}'


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    last_modified = db.Column(db.DateTime())
    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())
    creator_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __str__(self):
        return f'{self.title} - {self.description}'


class Stage(db.Model):
    __tablename__ = 'stages'

    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    last_modified = db.Column(db.DateTime())
    title = db.Column(db.String())
    description = db.Column(db.String())
    event_id = db.Column(db.Integer(), db.ForeignKey('events.id'))
    responsible = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __str__(self):
        return f'{self.title} - {self.description} - Event {self.event_id}'


class Performance(db.Model):
    __tablename__ = 'performances'

    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    last_modified = db.Column(db.DateTime())
    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())
    order = db.Column(db.Integer())
    duration = db.Column(db.Interval())
    person = db.Column(db.Integer(), db.ForeignKey('users.id'))
    stage = db.Column(db.Integer(), db.ForeignKey('stages.id'))

    def __str__(self):
        return f'{self.title} - {self.description} - Person {self.person} - Stage {self.stage}'


class Material(db.Model):
    __tablename__ = 'materials'

    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    last_modified = db.Column(db.DateTime())
    title = db.Column(db.String())
    description = db.Column(db.String())
    storage_url = db.Column(db.Unicode())
    performance = db.Column(db.Integer(), db.ForeignKey('performances.id'))

    def __str__(self):
        return f'{self.title} - {self.description}'
