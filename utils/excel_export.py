import pandas as pd


async def export_users(pool):

    async with pool.acquire() as conn:

        rows = await conn.fetch(

            """
            SELECT
            created_at,
            first_name,
            subscribed,
            invited_count,
            bonus_received
            FROM users
            """
        )

    data = [dict(row) for row in rows]

    df = pd.DataFrame(data)

    file = "users.xlsx"

    df.to_excel(file, index=False)

    return file
