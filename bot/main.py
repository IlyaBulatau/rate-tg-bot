from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

import config as conf


dp = Dispatcher()
bot = Bot(token=conf.BOT_TOKEN)
app = web.Application()


async def on_startup(bot: Bot):
    await bot.set_webhook(f"{conf.PROXY_SERVER}/{conf.WEBHOOK_URL}/",secret_token=conf.SECRET_TOKEN)


###
from aiogram import Router
from aiogram.filters import CommandStart
r = Router()
@r.message(CommandStart())
async def handler(message):
    await message.answer("HELLO")
###

async def handler_webhook(request):
    print(request)
    update_data = await request.json()
    update_event = Update(**update_data)
    await dp.feed_update(bot=bot, update=update_event)
    # await dp._process_update(bot=bot, update=update_event)
    return web.Response(status=200)


def main():
    dp.startup.register(on_startup)
    dp.include_router(r)
    app.router.add_post(f"/{conf.WEBHOOK_URL}/", handler_webhook)

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=conf.SECRET_TOKEN,
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=f"/{conf.WEBHOOK_URL}")

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host=conf.BOT_HOST, port=int(conf.BOT_PORT))

if __name__ == "__main__":
    main()