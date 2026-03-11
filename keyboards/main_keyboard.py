from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_keyboard():

    return InlineKeyboardMarkup(

        inline_keyboard=[

            [InlineKeyboardButton(
                text="Что нужно сделать?",
                callback_data="instructions"
            )]

        ]

    )
