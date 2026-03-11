import os
import asyncpg


async def create_pool():

    return await asyncpg.create_pool(
        dsn=os.getenv("DATABASE_URL")
        ssl="require"
    )
