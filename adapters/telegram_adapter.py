from aiogram import Bot
from config import BOT_TOKEN


bot = Bot(BOT_TOKEN)


async def send_message(user_id, text):

    await bot.send_message(user_id, text)
    ref_link = await start_user(db, user_id)

    text = f"""
    Ваша реферальная ссылка:
    {ref_link}
    Пригласите 3 друзей и получите бонус.
    """
    await bot.send_message(user_id, text)

