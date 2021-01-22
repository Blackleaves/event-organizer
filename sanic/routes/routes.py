from app import app
from sanic.response import json


@app.route("/")
async def test(request):
    return json({"hello": "world"})


@app.route("/healthcheck")
async def healthcheck(request):
    return json("healthcheck")
