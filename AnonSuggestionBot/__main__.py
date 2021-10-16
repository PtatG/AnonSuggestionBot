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
async def index(request):
    return web.FileResponse('./AnonSuggestionBot/static/index.html')


@routes.post('/login')
async def login(request):
    data = await request.post()
    repo = data['repository']
    message = data['suggestion']
    #print(repo + ' ' + message)

    #return web.FileResponse('./AnonSuggestionBot/static/index.html')
    return web.Response(text=f'{repo} and {message}')

if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    port = os.environ.get("PORT")
    if port is not None:
        port = int(port)

    web.run_app(app, port=port)