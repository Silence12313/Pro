async def check_subscription(bot, user_id, channel):

    try:

        member = await bot.get_chat_member(
            f"@{channel}",
            user_id
        )

        return member.status in [
            "member",
            "administrator",
            "creator"
        ]

    except:

        return False
