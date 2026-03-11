import uuid
from config import BOT_USERNAME


def generate_referral_code():

    return str(uuid.uuid4())[:8]


def generate_referral_link(code):

    return f"https://t.me/{BOT_USERNAME}?start={code}"
