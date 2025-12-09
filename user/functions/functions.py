from aiogram import Bot, types 
from config import ADMIN


async def startup(bot : Bot):
    await bot.send_message(ADMIN, "Bot ishga tushdi ✅")
    print("Bot ishga tushdi ✅")

async def shutdown(bot : Bot):
    await bot.send_message(ADMIN, "Bot ishdan to'xtadi ❌")
    print("Bot ishdan to'xtadi ❌")

async def start_answer(message : types.Message, bot : Bot):
    await bot.send_message(message.from_user.id, f"Assalomu alaykum, {message.from_user.full_name} hush kelibsiz!")