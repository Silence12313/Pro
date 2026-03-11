from config import CHANNEL_USERNAME


async def check_subscription(bot, user_id):

    member = await bot.get_chat_member(
        chat_id=f"@{CHANNEL_USERNAME}",
        user_id=user_id
    )

    return member.status in ["member", "administrator", "creator"]
