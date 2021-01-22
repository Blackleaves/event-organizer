from sanic import Sanic
from gino.ext.sanic import Gino
import asyncio


app = Sanic(name='event_organizer')
app.config.DB_HOST = 'localhost'
app.config.DB_DATABASE = 'gino'
app.config['DB_USER'] = 'postgres'
app.config['DB_PASSWORD'] = 'thisisnewsecurepassword'


db = Gino()
db.init_app(app)
loop = asyncio.get_event_loop()
loop.run_until_complete(db.set_bind('postgresql://vihovin:somenewpassword@localhost/gino'))
from models.user import User
from models.role import Role
from models.event import Event
from models.stage import Stage
from models.perfomance import Perfomance
from models.materials import Material
loop.run_until_complete(db.gino.create_all())
