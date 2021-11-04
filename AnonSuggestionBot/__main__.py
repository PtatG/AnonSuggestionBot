import os
import requests
import json

import aiohttp
from aiohttp import web

import discord
from discord import Webhook, RequestsWebhookAdapter, File

routes = web.RouteTableDef()
Webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN,\
    adapter=RequestsWebhookAdapter())

# Site Navigation
@routes.get('/')
async def index(request):
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
    
    Webhook.send(message)


    return web.FileResponse('./AnonSuggestionBot/static/index.html')

if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    port = os.environ.get("PORT")
    if port is not None:
        port = int(port)

    web.run_app(app, port=port)

# TODO with this bot:
'''
 - read in repo name and suggestion
 - find discord webhook associated with repo name
 - send suggestion via webhook
'''