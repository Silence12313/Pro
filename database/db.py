import os
import asyncpg


async def create_pool():

    pool = await asyncpg.create_pool(
        dsn=os.getenv("DATABASE_URL")
    )

    return pool
