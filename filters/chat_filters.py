from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

from data.config import ADMINS


class IsGroup(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        return isinstance(message.chat.type, types.ChatType.GROUP)


class IsAdmin(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        return message.from_user.id in ADMINS
