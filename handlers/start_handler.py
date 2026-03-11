from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()
from services.referral_service import generate_ref_code
from aiogram.filters import CommandStart


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):

    try:

        data = await request.json()

        update = Update(**data)

        await dp.feed_update(bot, update)

        return {"ok": True}

    except Exception as e:

        print("Webhook error:", e)

        return {"ok": False}


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Бот работает 🚀")

async def start_user(db, user_id, ref_code):
    
    user = await db.fetchrow(
        "SELECT * FROM users WHERE telegram_id=$1",
        user_id
    )

    if user:
        return

    new_code = generate_ref_code()

    referrer_id = None

    if ref_code:

        ref = await db.fetchrow(
            "SELECT * FROM users WHERE ref_code=$1",
            ref_code
        )

        if ref:

            referrer_id = ref["telegram_id"]

    await db.execute(
        """
        INSERT INTO users(
            telegram_id,
            ref_code,
            referrer_id
        )
        VALUES($1,$2,$3)
        """,
        user_id,
        new_code,
        referrer_id
    )

from services.referral_service import generate_ref_code, generate_ref_link


async def start_user(db, user_id):

    user = await db.fetchrow(
        "SELECT * FROM users WHERE telegram_id=$1",
        user_id
    )

    if user:

        ref_link = generate_ref_link(user["ref_code"])

        return ref_link

    ref_code = generate_ref_code()

    await db.execute(
        """
        INSERT INTO users(telegram_id, ref_code)
        VALUES($1,$2)
        """,
        user_id,
        ref_code
    )

    ref_link = generate_ref_link(ref_code)

    return ref_link
