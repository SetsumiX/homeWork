from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TG_TOKEN")
if not TOKEN:
    raise ValueError("Токен не был найден")