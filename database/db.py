import os
import asyncpg

pool = None


async def create_pool():

    global pool

    pool = await asyncpg.create_pool(
        dsn=os.getenv("DATABASE_URL")
    )

    return pool


def get_pool():

    return pool
