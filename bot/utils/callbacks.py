from aiogram.filters.callback_data import CallbackData

from enum import Enum


class Action(Enum):
    CLICK = "click"


class Event(Enum):
    CURRENCY_TODAY = "currency_today"


class UserCallbackFactory(CallbackData, prefix="user"):
    action: Action
    event: str
