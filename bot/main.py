from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

import config as conf
from events import BOT_ROUTERS


dp = Dispatcher()
bot = Bot(token=conf.BOT_TOKEN)
app = web.Application()

async def on_startup(bot: Bot):
    await bot.set_webhook(
        f"{conf.PROXY_SERVER}/{conf.WEBHOOK_URL}/", 
        secret_token=conf.SECRET_TOKEN, 
        drop_pending_updates=True, 
        request_timeout=5,
        )

async def handler_webhook(request):
    update_data = await request.json()
    update_event = Update(**update_data)
    await dp.feed_update(bot=bot, update=update_event)
    return web.Response(status=200)


def main():
    dp.startup.register(on_startup)
    app.router.add_post(f"/{conf.WEBHOOK_URL}/", handler_webhook)
    dp.include_routers(*BOT_ROUTERS)

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=conf.SECRET_TOKEN,
    )
    webhook_requests_handler.register(app, path=f"/{conf.WEBHOOK_URL}")

    setup_application(app, dp, bot=bot)
    web.run_app(app, host=conf.BOT_HOST, port=int(conf.BOT_PORT))

if __name__ == "__main__":
    main()