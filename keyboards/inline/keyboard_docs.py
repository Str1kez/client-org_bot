from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


callback_back = CallbackData('get', 'back')
back = InlineKeyboardButton('Назад', callback_data=callback_back.new(back='back'))

callback_docs = CallbackData('get', 'type', 'name')
keyboard_docs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('2НДФЛ за два года', callback_data=callback_docs.new(type="ndfl", name="2НДФЛ за два года"))],
    [InlineKeyboardButton('Копия трудовой', callback_data=callback_docs.new(type="copy", name="Копия трудовой"))],
    [InlineKeyboardButton('Справка с места работы', callback_data=callback_docs.new(type="work",
                                                                                    name="Справка с места работы"))]
])

callback_salary = CallbackData('get', 'solution', 'name')
keyboard_salary = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('c зарплатой', callback_data=callback_salary.new(solution="yes", name='c зарплатой')),
        InlineKeyboardButton('без зарплаты', callback_data=callback_salary.new(solution="no", name='без зарплаты'))
    ],
    [back]
])

callback_localization = CallbackData('get', 'local')
keyboard_localization = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('на русском', callback_data=callback_localization.new(local="на русском")),
        InlineKeyboardButton('на английском', callback_data=callback_localization.new(local="на английском"))
    ],
    [InlineKeyboardButton('на русском и английском',
                          callback_data=callback_localization.new(local="на русском и английском"))],
    [back]
])
