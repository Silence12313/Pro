from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from services.referral_service import generate_referral_code, generate_referral_link
from services.subscription_service import check_subscription

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):

    user_id = message.from_user.id
    first_name = message.from_user.first_name

    args = message.text.split()

    referral_code = None

    if len(args) > 1:
        referral_code = args[1]

    pool = message.bot.get("db")

    async with pool.acquire() as conn:

        user = await conn.fetchrow(
            "SELECT * FROM users WHERE telegram_id=$1",
            user_id
        )

        if not user:

            code = generate_referral_code()

            await conn.execute(

                """
                INSERT INTO users
                (telegram_id, first_name, referral_code, invited_by)

                VALUES ($1,$2,$3,$4)
                """,

                user_id,
                first_name,
                code,
                referral_code
            )

            if referral_code:

                inviter = await conn.fetchrow(
                    "SELECT * FROM users WHERE referral_code=$1",
                    referral_code
                )

                if inviter:

                    await conn.execute(

                        """
                        UPDATE users
                        SET invited_count = invited_count + 1
                        WHERE referral_code=$1
                        """,

                        referral_code
                    )

        user = await conn.fetchrow(
            "SELECT * FROM users WHERE telegram_id=$1",
            user_id
        )

        link = generate_referral_link(user["referral_code"])

    text = f"""
Рады видеть вас, {first_name}!

Ваша реферальная ссылка:

{link}

Пригласите 3 друзей и получите бонус.
"""

    await message.answer(text)
