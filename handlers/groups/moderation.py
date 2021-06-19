from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

import re
import datetime

from loader import dp, bot
from data import get_read_only_permission


@dp.message_handler(Command("kick", prefixes="!/"), is_reply=True)
async def kick_user(message: Message):
    admin_mention = message.from_user.get_mention(as_html=True)

    member_id = message.reply_to_message.from_user.id
    member_status = (await message.chat.get_member(member_id)).status
    member_mention = message.reply_to_message.from_user.get_mention(as_html=True)
    if member_status == "left":
        await message.answer(f"The user {member_mention} isn't a member of the group.")
        return

    bot_username = (await bot.get_me()).username

    command_parse = re.compile(fr"(!kick|/kick)(@{bot_username})? ([\w+\D]+)?")
    parse = command_parse.match(message.text)

    reason = parse.group(3)
    if reason:
        reason = f"\nReason: {reason}"
    else:
        reason = "without mention reason"

    try:
        await message.chat.kick(member_id)
        await message.answer(f"User {member_mention} "
                             f"was kicked by {admin_mention} {reason}")

    except BadRequest:
        await message.answer(f"User {member_mention} is an administrator.\n"
                             f"You can't do that.")





# @dp.message_handler(Command("mute", prefixes="!/"), is_reply=True)
# async def mute_user(message: Message):
#     admin_mention = message.from_user.get_mention(as_html=True)
#
#     member_id = message.reply_to_message.from_user.id
#     member_status = (await message.chat.get_member(member_id)).status
#     member_mention = message.reply_to_message.from_user.get_mention(as_html=True)
#     if member_status == "left":
#         await message.answer(f"The user {member_mention} isn't a member of the group.")
#         return
#
#     bot_username = (await bot.get_me()).username
#
#     command_parse = re.compile(fr"(!mute|/mute)(@{bot_username})? (\d+)? ?([\w+\D]+)?")
#     parse = command_parse.match(message.text)
#
#     time = parse.group(3)
#     reason = parse.group(4)
#     if not time:
#         time = 15
#
#     if reason:
#         reason = f"\nReason: {reason}"
#     else:
#         reason = "without a mention reason"
#
#     # try:
#     until_time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
#     await bot.restrict_chat_member(
#         chat_id=message.chat.id,
#         user_id=member_id,
#         permissions=get_read_only_permission(),
#         until_date=until_time
#     )
#     await message.answer(f"The user {member_mention} "
#                              f"was muted by {admin_mention} "
#                              f"for {time} minutes {reason}")
    #
    # except BadRequest:
    #     await message.answer(f"User {member_mention} is an administrator.\n"
    #                          f"You can't do that.")

