from aiogram import Bot, Dispatcher, types, F
from config import API_TOKEN
from user.functions.functions import startup, shutdown, start_answer
from asyncio import run
from aiogram.types import BotCommand
from aiogram.filters import CommandStart



async def start():
    bot = Bot(API_TOKEN)
    dp = Dispatcher()

    dp.startup.register(startup)
    dp.message.register(start_answer, CommandStart)
    dp.shutdown.register(shutdown)

    await bot.set_my_commands(
        [
            BotCommand(command='/start', description="Botni qayta ishga tushirish!"),
            BotCommand(command = "/help", description="Yordam so'rash!")
        ]
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    run(start())
