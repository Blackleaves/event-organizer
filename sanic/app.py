from gino.ext.sanic import Gino
from sanic import Sanic


app = Sanic(name='event_organizer')
app.config.from_envvar('MYAPP_SETTINGS')
db = Gino()
