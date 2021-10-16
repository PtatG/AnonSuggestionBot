import os
import aiohttp

from aiohttp import web
from gidgethub import routing, sansio
from pymongo import MongoClient
from pprint import pprint

#url = os.environ.get("MDB_URL")

#client = MongoClient(url)
#db = client.issueBot

router = routing.Router()

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")

if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    port = os.environ.get("PORT")
    if port is not None:
        port = int(port)

    web.run_app(app, port=port)