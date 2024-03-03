from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.keyboards import buttons
from domains.currencies import AvalibaleCurrency


def start_command_keyboard(builder_type = InlineKeyboardBuilder):
    builder = builder_type()
    builder.add(buttons.currency_today_button)
    return builder.as_markup()

def currency_callback_keyboard(builder_type = InlineKeyboardBuilder):
    builder = builder_type()
    builder.row(
        *[
            buttons.abbreviation_currency_button(abbreviation) 
            for abbreviation in AvalibaleCurrency.to_list()
            ],
        width=2,
    )
    return builder.as_markup()