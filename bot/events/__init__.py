from events.commands.handlers import router as commands_router
from events.currenccies.handler import router as currency_router


BOT_ROUTERS = [
    commands_router,
    # currency_router,
]