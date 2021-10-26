from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types

from keyboards.inline import keyboard_docs
from loader import dp
from states import Docs


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nВыбери необходимый документ",
                         reply_markup=keyboard_docs)
    await Docs.name.set()
