from openpyxl import Workbook


async def export_users_to_excel(db):

    users = await db.fetch(
        "SELECT * FROM users"
    )

    wb = Workbook()

    ws = wb.active

    ws.append([
        "дата",
        "клиент",
        "подписан ли на канал",
        "количество приглашенных людей",
        "полученные бонусы"
    ])

    for user in users:

        count = await db.fetchval(
            """
            SELECT COUNT(*)
            FROM referrals
            WHERE referrer_id=$1
            """,
            user["telegram_id"]
        )

        ws.append([
            user["created_at"].strftime("%Y-%m-%d"),
            user["telegram_id"],
            "unknown",
            count,
            "Да" if user["bonus_sent"] else "Нет"
        ])

    file = "users_export.xlsx"

    wb.save(file)

    return file
