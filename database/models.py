async def init_db(pool):

    async with pool.acquire() as conn:

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS users (

            id SERIAL PRIMARY KEY,

            telegram_id BIGINT UNIQUE,

            first_name TEXT,

            referral_code TEXT UNIQUE,

            invited_by TEXT,

            invited_count INTEGER DEFAULT 0,

            subscribed BOOLEAN DEFAULT FALSE,

            bonus_received BOOLEAN DEFAULT FALSE,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

        """)
