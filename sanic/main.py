from sanic.exceptions import abort
from sanic.response import json
from app import app
from routes import routes


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
