from services.export_service import export_users_to_excel
from config import ADMIN_ID


async def export_users(message, db):

    if message.from_user.id != ADMIN_ID:
        return

    file = await export_users_to_excel(db)

    await message.answer_document(file)
