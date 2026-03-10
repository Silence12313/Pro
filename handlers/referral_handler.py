from services.referral_service import count_referrals
from config import REFERRALS_REQUIRED


async def process_referral(db, user_id):

    count = await count_referrals(db, user_id)

    if count == 1:

        return "Приглашен первый друг!"

    if count == 2:

        return "Приглашено два друга!"

    if count >= REFERRALS_REQUIRED:

        await db.execute(
            """
            UPDATE users
            SET bonus_sent=TRUE
            WHERE telegram_id=$1
            """,
            user_id
        )

        return "Поздравляем! Вот ваш бонус."
