import random
import string


def generate_ref_code():

    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=8
        )
    )


async def count_referrals(db, user_id):

    return await db.fetchval(
        """
        SELECT COUNT(*)
        FROM referrals
        WHERE referrer_id=$1
        """,
        user_id
    )

from config import BASE_REF_URL


def generate_ref_link(ref_code):

    return f"{BASE_REF_URL}{ref_code}"

import random
import string


def generate_ref_code():

    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=8
        )
    )
