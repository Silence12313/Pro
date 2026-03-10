from fastapi import FastAPI, Request
import uvicorn
import os

from database.db import create_pool
from database.models import init_db

import asyncio
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
app = FastAPI()

db = None


@app.on_event("startup")
async def startup():
    global db
    db = await create_pool()

    asyncio.create_task(dp.start_polling(bot))


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):

    data = await request.json()

    print(data)

    return {"ok": True}


@app.post("/max/webhook")
async def max_webhook(request: Request):

    data = await request.json()

    print(data)

    return {"ok": True}


if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000))
    )
