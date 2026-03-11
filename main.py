import os
from fastapi import FastAPI, Request
import uvicorn


from handlers.start_handler import router as start_router

dp.include_router(start_router)


from aiogram import Bot, Dispatcher
from aiogram.types import Update

from config import BOT_TOKEN
from database.db import create_pool
from database.models import init_db

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

app = FastAPI()

db = None


@app.on_event("startup")
async def startup():

    global db

    db = await create_pool()
    await init_db(db)


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):

    data = await request.json()

    update = Update(**data)

    await dp.feed_update(bot, update)

    return {"ok": True}


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
