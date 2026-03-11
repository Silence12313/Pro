import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_USERNAME = os.getenv("BOT_USERNAME")

CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

REFERRALS_REQUIRED = 3

BONUS_LINK = "https://www.youtube.com/playlist?list=PL2DjtAFoLP6w3ztMXg4eLzBPUj3iaFvPm"

CONSULT_LINK = "https://onstudy.org/konsultatsiya-art/"

TELEGRAM_REF_LINK = f"https://t.me/{BOT_USERNAME}?start=" if BOT_USERNAME else None
