from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.keyboards import buttons


def start_command_keyboard(builder = InlineKeyboardBuilder()):
    builder.add(buttons.currency_today_button)
    return builder.as_markup()