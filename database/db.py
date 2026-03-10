import asyncpg
import os


async def create_pool():

    return await asyncpg.create_pool(
        user=os.getenv("DB_USER"),
        dsn=os.getenv("DATABASE_URL"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST")
    )
