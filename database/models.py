async def init_db(db):

    await db.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id SERIAL PRIMARY KEY,

        telegram_id BIGINT,

        max_id TEXT,

        ref_code TEXT,

        referrer_id BIGINT,

        bonus_sent BOOLEAN DEFAULT FALSE,

        created_at TIMESTAMP DEFAULT NOW()

    )
    """)

    await db.execute("""
    CREATE TABLE IF NOT EXISTS referrals(

        id SERIAL PRIMARY KEY,

        referrer_id BIGINT,

        invited_id BIGINT,

        created_at TIMESTAMP DEFAULT NOW()

    )
    """)
