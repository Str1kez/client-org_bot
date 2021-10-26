from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from keyboards.inline import callback_docs, callback_salary, keyboard_salary, callback_localization, \
    keyboard_localization, keyboard_docs, callback_back
from loader import dp
from .start import Docs


@dp.callback_query_handler(callback_back.filter(back='back'), state=Docs.with_salary)
async def back_to_begin(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.reset_state()
    await call.message.edit_text(f"Привет, {call.message.from_user.full_name}!\nВыбери необходимый документ",
                         reply_markup=keyboard_docs)
    await Docs.name.set()


@dp.callback_query_handler(callback_back.filter(back='back'), state=Docs.localization)
async def back_to_salary(call: CallbackQuery, state: FSMContext):
    await call.answer()
    print(await state.get_data())
    await call.message.edit_text(f'Выберите:')
    await call.message.edit_reply_markup(keyboard_salary)
    await Docs.with_salary.set()


@dp.callback_query_handler(callback_docs.filter(type='ndfl'), state=Docs.name)
async def ndfl_chosen(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    await state.update_data(name=callback_data["name"])
    await call.message.edit_text(f'Выберите локацию:')
    await call.message.edit_reply_markup()
    await Docs.location.set()


@dp.callback_query_handler(callback_docs.filter(type='copy'), state=Docs.name)
async def copy_chosen(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    await state.update_data(name=callback_data["name"])
    await call.message.edit_text(f'Выберите локацию:')
    await call.message.edit_reply_markup()
    await Docs.location.set()


@dp.callback_query_handler(callback_docs.filter(type='work'), state=Docs.name)
async def sertificate_chosen(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    await state.update_data(name=callback_data["name"])
    await call.message.edit_text(f'Выберите:')
    await call.message.edit_reply_markup(keyboard_salary)
    await Docs.with_salary.set()


@dp.callback_query_handler(callback_salary.filter(), state=Docs.with_salary)
async def sertificate_chosen(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    await state.update_data(with_salary=callback_data["name"])
    await call.message.edit_reply_markup(keyboard_localization)
    await Docs.localization.set()


@dp.callback_query_handler(callback_localization.filter(), state=Docs.localization)
async def sertificate_chosen(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    await state.update_data(localization=callback_data["local"])
    # ORG_DATA['Хабаровск']['HR2']['email'] = 'WOOOOOOOOOOOOOOW'
    # with open('utils/db_api/base.json', 'w', encoding='utf-8') as f:
    #     json.dump(ORG_DATA, f, indent=4, ensure_ascii=False)
    await call.message.edit_reply_markup()
    await Docs.location.set()
