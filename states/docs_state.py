from aiogram.dispatcher.filters.state import StatesGroup, State


class Docs(StatesGroup):
    name = State()
    with_salary = State()
    localization = State()
    location = State()
    add_location = State()
    user_data = State()
