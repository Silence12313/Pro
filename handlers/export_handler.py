from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from utils.excel_export import export_users

router = Router()


@router.message(Command("export"))
async def export_data(message: Message):

    pool = get_pool()

    file = await export_users(pool)

    await message.answer_document(open(file, "rb"))
