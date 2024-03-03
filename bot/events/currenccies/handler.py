from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from utils.callbacks import UserCallbackFactory, Event
from domains.currencies import AvalibaleCurrency
from utils.keyboards import currency_callback_keyboard


router = Router()

@router.callback_query(UserCallbackFactory.filter(F.event==Event.CURRENCY_TODAY.value))
async def callback_get_currency_today(callback: CallbackQuery, callback_data: UserCallbackFactory, bot: Bot):
    """Нажатие кнопки 'Курс на сегодня'"""
    await callback.answer()
    await callback.message.answer(text="TODAY", reply_markup=currency_callback_keyboard())
