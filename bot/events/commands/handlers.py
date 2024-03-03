from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.keyboards import start_command_keyboard


router = Router()

@router.message(CommandStart())
async def start_command_handler(message: Message):
    await message.answer("Выберите действие", reply_markup=start_command_keyboard())