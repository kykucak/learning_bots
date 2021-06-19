from aiogram import Dispatcher

from loader import dp
from .chat_filters import IsAdmin, IsGroup


if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsGroup)
