from aiogram import Router
from aiogram.types import Message

from config import REFERRALS_REQUIRED, BONUS_LINK
from services.subscription_service import check_subscription

router = Router()


@router.message()
async def referral_progress(message: Message):

    user_id = message.from_user.id

    pool = message.bot.get("db")

    async with pool.acquire() as conn:

        user = await conn.fetchrow(
            "SELECT * FROM users WHERE telegram_id=$1",
            user_id
        )

        if not user:
            return

        invited = user["invited_count"]

        if invited == 1:

            await message.answer(
                "Приглашен первый друг. Отлично!"
            )

        if invited == 2:

            await message.answer(
                "Уже два друга! Остался один."
            )

        if invited >= REFERRALS_REQUIRED and not user["bonus_received"]:

            subscribed = await check_subscription(
                message.bot,
                user_id
            )

            if not subscribed:

                await message.answer(
                    "Подпишитесь на канал чтобы получить бонус"
                )

                return

            await conn.execute(

                """
                UPDATE users
                SET bonus_received=TRUE
                WHERE telegram_id=$1
                """,

                user_id
            )

            await message.answer(

f"""
Поздравляем!

Вы получили бонус.

{BONUS_LINK}
"""
            )
