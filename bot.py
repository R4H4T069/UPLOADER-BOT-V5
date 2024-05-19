import logging
import os
from plugins.config import Config
from pyrogram import Client as Ntbots
from pyrogram import filters
from aiohttp import web
import asyncio

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Web server handler
async def handle(request):
    return web.Response(text="Bot is running")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    logger.info("Web server started on port 8080")

# Bot and web server runner
async def main():
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    
    plugins = dict(root="plugins")
    bot = Ntbots(
        "URL UPLOADER BOT",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    
    # Start the web server
    asyncio.create_task(start_web_server())
    
    # Start the bot
    await bot.start()
    me = await bot.get_me()
    logger.info(f"{me.first_name} is started.....✨️")
    await bot.idle()  # Keep the bot running

if __name__ == "__main__":
    asyncio.run(main())
