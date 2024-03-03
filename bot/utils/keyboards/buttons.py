from aiogram.types import InlineKeyboardButton

from utils.callbacks import UserCallbackFactory, Action, Event


currency_today_button = InlineKeyboardButton(
    text="Курс на сегодня", 
    callback_data=UserCallbackFactory(
        action=Action.CLICK.value, 
        event=Event.CURRENCY_TODAY.value
        ).pack()
    )

abbreviation_currency_button = lambda abbreviation: InlineKeyboardButton(
    text=abbreviation,
    callback_data=UserCallbackFactory(
        action=Action.CLICK.value,
        event=abbreviation
    ).pack()
)