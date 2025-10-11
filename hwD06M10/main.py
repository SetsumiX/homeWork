from aiogram import Bot,Dispatcher
from aiogram.types import BotCommand
import asyncio
from config import TOKEN_BOT
from handler.commands import router

bot = Bot(token=TOKEN_BOT)
disp = Dispatcher()

async def active_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запуск бота"),
    ]
    await bot.set_my_commands(commands)

async def main():
    try:
        await active_commands(bot)
        disp.include_router(router)
        await disp.start_polling(bot)
    except KeyboardInterrupt:
        print("Выключение бота")
    finally:
        await bot.session.close()
        print("Закрытие сессии")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Выключение бота")