from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
import asyncio

bot = Bot(token=BOT_TOKEN)
disp = Dispatcher()

@disp.message(CommandStart())
async def start_handler(message: types.Message):
    botinf = await bot.get_me()
    await message.answer(f"Бот {botinf.first_name} приветствует вас, {message.from_user.full_name}")

@disp.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer(f"Для использования, доступны:\n"
                         f"/start - Запуск бота.\n"
                         f"/music - Тот самый любимый жанр музыки, который слушает автор бота.\n"
                         f"/help - Справочник команд.\n")

@disp.message(Command("music"))
async def send_sewerslvt_handler(message: types.Message):
    audio = FSInputFile("./audio/Sewerslvt-Squids.m4a")
    await message.reply_audio(
        audio,
        caption="🎵Абсолютный кайф в жанре Breakcore🎵"
    )

async def main():
    try:
        await disp.start_polling(bot)
    except KeyboardInterrupt:
        print("Выключение")
    finally:
        await bot.session.close()
        print("Сессия закрыта")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Выключение")