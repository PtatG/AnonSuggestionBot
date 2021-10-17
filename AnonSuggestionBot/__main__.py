import os
import aiohttp
import asyncio

from aiohttp import web
from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp
from pymongo import MongoClient
from pprint import pprint

#url = os.environ.get("MDB_URL")

#client = MongoClient(url)
#db = client.issueBot

router = routing.Router()

routes = web.RouteTableDef()

# Site Navigation
@routes.get('/')
async def index(request):


        # maybe i need nothing here..?

    return web.FileResponse('./AnonSuggestionBot/static/index.html')

@routes.get('/index.html')
async def index(request):
    #return web.Response()
    return web.FileResponse('./AnonSuggestionBot/static/index.html')

@routes.get('/html/commit.html')
async def commit(request):
    #return web.Response()
    return web.FileResponse('./AnonSuggestionBot/static/html/commit.html')

@routes.get('/html/gamification.html')
async def gamification(request):
    #return web.Response()
    return web.FileResponse('./AnonSuggestionBot/static/html/gamification.html')

@routes.get('/html/anonymous.html')
async def anonymous(request):
    #return web.Response()
    return web.FileResponse('./AnonSuggestionBot/static/html/anonymous.html')

# Server Processes
@routes.post('/login')
async def login(request):
    data = await request.post()
    repo = data['repository']
    message = data['suggestion']
    
    oauth_token = os.environ.get("GH_AUTH")

    async with aiohttp.ClientSession() as session:
        gh = gh_aiohttp.GitHubAPI(session, "alexogilbee",
                                  oauth_token=oauth_token)
    
        await asyncio.sleep(5)

    url = "https://api.github.com/repos/alexogilbee/githubbottest/discussions/7/comments"

    await gh.post(url, data={'body': message})
    #return web.FileResponse('./AnonSuggestionBot/static/index.html')
    return web.Response(text=f'{repo} and {message}')

if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    port = os.environ.get("PORT")
    if port is not None:
        port = int(port)

    web.run_app(app, port=port)