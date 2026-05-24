from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler

from api import get_matches
from analyzer import analyze_match
from signal import is_banko, is_kg, is_over, ai_score

# =========================================
# PANEL GÖSTER
# =========================================

def get_panel():
    keyboard = [

        [InlineKeyboardButton("📊 Canlı Maçlar", callback_data="live")],
        [InlineKeyboardButton("🔥 Banko Kupon", callback_data="banko")],

        [
            InlineKeyboardButton("⚽ KG VAR", callback_data="kg"),
            InlineKeyboardButton("🚀 ÜST 2.5", callback_data="over")
        ],

        [InlineKeyboardButton("🤖 AI Skor", callback_data="ai")]
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================================
# CALLBACK HANDLER
# =========================================

def handle_buttons(update, context):

    query = update.callback_query
    query.answer()

    data = query.data

    matches = get_matches()

    # =====================================
    # CANLI MAÇLAR
    # =====================================

    if data == "live":

        text = ""

        for m in matches:

            if m["fixture"]["status"]["short"] in ["1H", "HT", "2H", "LIVE"]:

                h = m["teams"]["home"]["name"]
                a = m["teams"]["away"]["name"]

                text += f"⚽ {h} vs {a}\n"

        query.edit_message_text("📊 CANLI MAÇLAR\n\n" + text[:3500])

    # =====================================
    # BANKO
    # =====================================

    elif data == "banko":

        text = "🔥 BANKO KUAPON\n\n"

        for m in matches:

            if is_banko(m):

                h = m["teams"]["home"]["name"]
                a = m["teams"]["away"]["name"]

                text += f"💎 {h} vs {a}\n"

        query.edit_message_text(text[:3500])

    # =====================================
    # KG VAR
    # =====================================

    elif data == "kg":

        text = "⚽ KG VAR MAÇLAR\n\n"

        for m in matches:

            if is_kg(m):

                h = m["teams"]["home"]["name"]
                a = m["teams"]["away"]["name"]

                text += f"⚽ {h} vs {a}\n"

        query.edit_message_text(text[:3500])

    # =====================================
    # ÜST 2.5
    # =====================================

    elif data == "over":

        text = "🚀 ÜST 2.5 MAÇLAR\n\n"

        for m in matches:

            if is_over(m):

                h = m["teams"]["home"]["name"]
                a = m["teams"]["away"]["name"]

                text += f"🔥 {h} vs {a}\n"

        query.edit_message_text(text[:3500])

    # =====================================
    # AI SKOR
    # =====================================

    elif data == "ai":

        text = "🤖 AI GÜVEN SKORU\n\n"

        for m in matches[:10]:

            h = m["teams"]["home"]["name"]
            a = m["teams"]["away"]["name"]

            score = ai_score(m)

            text += f"{h} vs {a} → %{score}\n"

        query.edit_message_text(text[:3500])
