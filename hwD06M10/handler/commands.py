from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from datetime import datetime
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from database.dbSystem import DBUser

router = Router()
db = DBUser()

@router.message(CommandStart())
async def start_handler(message: Message):
    current_time = datetime.now().strftime("%H:%M:%S, %d:%m:%Y")
    user = message.from_user
    tplInfo = (user.full_name, user.id, user.username, current_time)
    db.add_user(tplInfo)
    db.get_info()
    await message.answer(f"Здравствуй, {message.from_user.full_name}")