from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types

from loader import dp
from states import Form


@dp.message_handler(Command("form"))
async def start_form(message: types.Message):
    await message.answer("You decided to fill the form!\n"
                         "Question #1\n"
                         "What's your name?")

    await Form.name.set()


@dp.message_handler(state=Form.name)
async def answer_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)

    await message.answer("Question #2\n"
                         "What's your email?")
    await Form.next()


@dp.message_handler(state=Form.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)

    await message.answer("Question #3\n"
                         "What's your number?")
    await Form.next()


@dp.message_handler(state=Form.phone)
async def answer_email(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    form_data = await state.get_data()

    await message.answer(f"Hello! You entered this data:\n\n"
                         f"Your name - {form_data.get('name')}\n"
                         f"Your email - {form_data.get('email')}\n"
                         f"Your number - {form_data.get('phone')}\n\n"
                         f"Thank you! Have a good day.")

    await state.reset_state(with_data=False)

