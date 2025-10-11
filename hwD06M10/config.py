import os
from dotenv import load_dotenv

load_dotenv()
TOKEN_BOT = os.getenv("TOKEN_BOT")
if not TOKEN_BOT:
    raise ValueError("Токен бота не найден")