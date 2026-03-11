import os
from fastapi import FastAPI, Request
import uvicorn

from aiogram import Bot, Dispatcher
from aiogram.types import Update

from config import BOT_TOKEN
from database.db import create_pool
from database.models import init_db

from handlers.start_handler import router as start_router
from handlers.referral_handler import router as referral_router
from handlers.export_handler import router as export_router

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(referral_router)
dp.include_router(export_router)

app = FastAPI()

db = None


@app.on_event("startup")
async def startup():

    global db

    db = await create_pool()

    await init_db(db)


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


@app.post("/max/webhook")
async def max_webhook(request: Request):

    data = await request.json()

    print("MAX event:", data)

    return {"ok": True}


if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000))
    )
