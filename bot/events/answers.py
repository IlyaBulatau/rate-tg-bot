from aiogram.types import CallbackQuery

from domains.dto import ExchangeRate


async def answer_rate_today(callback: CallbackQuery, rate: ExchangeRate) -> str:
    _format = "*{name_ru}*\n\nНа дату: {date}\nКурс: {rate} BYN\nЕдиниц валюты: {scale} {abbreviation}\n"
    answer = _format.format(
        name_ru=rate.name_ru,
        date=rate.date,
        rate=round(float(rate.rate), 2),
        scale=rate.scale,
        abbreviation=rate.currency_abbreviation,
    )

    await callback.message.answer(text=answer, parse_mode="Markdown")
    return