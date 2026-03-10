import os

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")   # username бота без @

# MAX
MAX_TOKEN = os.getenv("MAX_TOKEN")

# Канал
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME", "your_art_muse")

# Реферальная система
REFERRALS_REQUIRED = int(os.getenv("REFERRALS_REQUIRED", 3))

# базовая ссылка Telegram
TELEGRAM_REF_LINK = f"https://t.me/{BOT_USERNAME}?start="

# универсальная реферальная ссылка (если есть домен)
BASE_REF_URL = os.getenv("BASE_REF_URL", TELEGRAM_REF_LINK)

# бонус
BONUS_URL = os.getenv(
    "BONUS_URL",
    "https://www.youtube.com/playlist?list=PL2DjtAFoLP6w3ztMXg4eLzBPUj3iaFvPm"
)

CONSULT_URL = os.getenv(
    "CONSULT_URL",
    "https://onstudy.org/konsultatsiya-art/"
)

# администратор
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
