import asyncio
import aiogram
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import TOKEN

bot = Bot(token=TOKEN)
disp = Dispatcher()

async def get_conversion(value: int, message: types.Message):
    url = "https://api.frankfurter.app/latest?from=USD&to=EUR"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    result = data["rates"]["EUR"] * value
                    return result
                else:
                    return f"Ошибка API: {response.status}"
    except Exception as e:
        return "Ошибка конвертации"

@disp.message(Command("get_convert"))
async def convert_handler(message: types.Message):
    try:
        parts = message.text.split()
        if len(parts) < 2:
            raise message.answer("Вы не ввели цифры после команды.\nПример написания: (команда) (количество валюты)")
        value = float(parts[1])
        result = await get_conversion(value, message)

        await message.answer(f"USD({value}) => EUR({result:.2f})")

    except ValueError:
        await message.answer("Вы ввели что-то по мимо цифр.\nПример написания: (команда) (количество валюты)")
    except Exception as err:
        print(f"Ошибка: {err}")
        await message.answer("Ошибка: Обработка запроса")

async def main():
    try:
        await bot.delete_my_commands()
        await disp.start_polling(bot)
    except KeyboardInterrupt:
        print("Остановка бота")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        await bot.session.close()
        print("Сессия закрыта")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Остановка бота")