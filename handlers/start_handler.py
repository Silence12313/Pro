from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):

    first_name = message.from_user.first_name

    text = f"""
Рады видеть вас, {first_name}!

Если вам нравится наш канал Your art muse — приглашайте друзей.

Пригласите 3 друзей и получите бонус.
"""

    await message.answer(text)
