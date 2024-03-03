from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from utils.callbacks import UserCallbackFactory, Event
from domains.currencies import AvalibaleCurrency
from utils.keyboards import currency_callback_keyboard
from services.use_case import get_all_currency


router = Router()

@router.callback_query(UserCallbackFactory.filter(F.event==Event.CURRENCY_TODAY.value))
async def callback_get_currency_today(callback: CallbackQuery, callback_data: UserCallbackFactory, bot: Bot):
    """Нажатие кнопки 'Курс на сегодня'"""
    await callback.answer()
    await callback.message.answer(text="TODAY", reply_markup=currency_callback_keyboard())


@router.callback_query(UserCallbackFactory.filter(F.event.in_(AvalibaleCurrency.to_list())))
async def callback_abbreviations(callback: CallbackQuery, callback_data: UserCallbackFactory, bot: Bot):
    await callback.answer()
    # r = await get_all_currency()
    await callback.message.answer(text="HELLO")
