from aiogram.dispatcher.filters import Command
from aiogram.types import Message, InputFile
from aiogram.utils.exceptions import BadRequest

import io

from loader import dp


@dp.message_handler(Command("set_title", prefixes="!/"))
async def set_new_title(message: Message):
    try:
        admin_mention = message.from_user.get_mention(as_html=True)

        new_title = message.reply_to_message.text

        await message.chat.set_title(new_title)
        await message.answer(f"The user {admin_mention} has changed a chat title")
    except BadRequest:
        await message.answer(f"Sorry, but it can't be a chat title")


@dp.message_handler(Command("set_photo", prefixes="!/"))
async def set_new_photo(message: Message):
    try:
        admin_mention = message.from_user.get_mention(as_html=True)

        new_photo = message.reply_to_message.photo[-1]
        new_photo = await new_photo.download(destination=io.BytesIO())
        input_photo = InputFile(path_or_bytesio=new_photo)

        await message.chat.set_photo(input_photo)
        await message.answer(f"The user {admin_mention} has changed a chat photo")
    except (BadRequest, IndexError):
        await message.answer(f"Sorry, but it can't be a chat photo")
