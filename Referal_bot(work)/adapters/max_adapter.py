import httpx
from config import MAX_TOKEN


async def send_max_message(user_id, text):

    url = "https://api.max.ru/messages"

    headers = {
        "Authorization": f"Bearer {MAX_TOKEN}"
    }

    data = {
        "user_id": user_id,
        "text": text
    }

    async with httpx.AsyncClient() as client:

        await client.post(url, json=data, headers=headers)
