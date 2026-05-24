from telegram import (
    Bot,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from config import BOT_TOKEN, CHAT_ID

bot = Bot(token=BOT_TOKEN)

# =========================================
# BUTONLU MESAJ
# =========================================

def send_panel():

    keyboard = [

        [
            InlineKeyboardButton(
                "📊 Canlı Maçlar",
                callback_data="live"
            )
        ],

        [
            InlineKeyboardButton(
                "🔥 Bankolar",
                callback_data="banko"
            )
        ],

        [
            InlineKeyboardButton(
                "⚽ KG VAR",
                callback_data="kgvar"
            ),

            InlineKeyboardButton(
                "🚀 ÜST 2.5",
                callback_data="over25"
            )
        ],

        [
            InlineKeyboardButton(
                "🏆 Büyük Ligler",
                callback_data="bigleagues"
            )
        ],

        [
            InlineKeyboardButton(
                "📈 Günün Kuponu",
                callback_data="coupon"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(
        chat_id=CHAT_ID,
        text="🤖 PRO IDDAA ANALİZ PANEL",
        reply_markup=reply_markup
    )

# =========================================
# NORMAL MESAJ
# =========================================

def send_message(text):

    bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )
