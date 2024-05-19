#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
from plugins.config import Config
from pyrogram import Client as Ntbots
from pyrogram import filters
from aiohttp import web

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

async def handle(request):
    return web.Response(text="Hello, world")

if name == "__main__":
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    
    plugins = dict(root="plugins")
    Ntbots = Ntbots(
        "UploadLinkToFileBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )

    # Define and get the port from environment variable
    port = int(os.getenv("PORT", 80))

    # Start the bot
    Ntbots.start()

    # Setting up a web server to listen on the port
    app = web.Application()
    app.router.add_get('/', handle)
    
    # Running the web server
    web.run_app(app, port=port)

    # Running the bot (this will block the code execution, so make sure it's last)
    Ntbots.run()
