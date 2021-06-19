from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start the bot"),
            types.BotCommand("help", "Get help info about the bot"),
            types.BotCommand("kick", "Kick user by reply message")
        ]
    )
