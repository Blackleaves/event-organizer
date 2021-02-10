import argparse
import os

from api import api
from app import app, db
from models import User, Role, Event, Stage, Performance, Material

# TO RUN USE THIS
# MYAPP_SETTINGS=~/Mentoree/event-organizer/sanic/config.py python sanic/main.py --host="0.0.0.0" --port=8080

parser = argparse.ArgumentParser("Parse arguments")
parser.add_argument("--host", type=str, required=True, help="DB Host")
parser.add_argument("--port", required=True, help="DB Host Port")

db_string = "postgresql://{}:{}@{}/{}".format(os.getenv('DB_USER', 'vihovin'),
                                              os.getenv('DB_PASSWORD', 'thisissomenewpass'),
                                              os.getenv('DB_HOST', 'localhost'),
                                              os.getenv('PG_DATABASE', 'gino'))


@app.listener('before_server_start')
async def before_server_start(app, loop):
    db.init_app(app)
    await db.set_bind(db_string)
    await db.gino.create_all()
    app.blueprint(api)


if __name__ == "__main__":
    # app.static('/', './')  <- this one caused the problem
    parsed_args = parser.parse_args()
    app.run(host=parsed_args.host, port=parsed_args.port)
