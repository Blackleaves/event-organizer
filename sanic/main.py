from sanic import Sanic
from sanic.response import json

from gino import Gino

import asyncio

app = Sanic()
app.config.DB_HOST = 'localhost'
app.config.DB_DATABASE = 'gino'
app.config['DB_USER'] = 'postgres'
db = Gino()
# db.init_app(app)

# -----------------------------------------

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.String(), default='noname')
    name = db.Column(db.String(), default='John Doe')
    email = db.Column(db.Unicode())
    description = db.Column(db.String())
    role = db.Column(db.Integer())

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())
    creator_id = db.Column(db.Integer())

class Stage(db.Model):
    __tablename__ = 'stages'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    event_id = db.Column(db.Integer())
    responsible = db.Column(db.Integer())

class Perfomance(db.Model):
    __tablename__ = 'perfomances'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    code = db.Column(db.Unicode())
    order = db.Column(db.Integer())
    duration = db.Column(db.Interval())
    stage = db.Column(db.Integer())

class Material(db.Model):
    __tablename__ = 'materials'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    storage_url = db.Column(db.Unicode())
    perfomance = db.Column(db.Integer())

# -----------------------------------------

@app.route("/")
async def test(request):
  return json({"hello": "world"})

@app.route("/healthcheck")
async def healthcheck(request):
	return json("healthcheck")

# -----------------------------------------

async def main():
    await db.set_bind('postgresql://localhost/gino')
asyncio.get_event_loop().run_until_complete(main())

loop.run_until_complete(db.gino.create_all())

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)