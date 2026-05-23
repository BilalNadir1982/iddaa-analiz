from api import get_matches
from analyzer import analyze_match
from sender import send_to_channel

def format_msg(match, analysis):
    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]

    ms = analysis["ms"]
    kg = analysis["kg"]
    over25 = analysis["over25"]
    ih = analysis["first_half"]

    return f"""
🔥 GÜNÜN İDDİA ANALİZİ 🔥

⚽ {home} - {away}

📊 MS: {ms}
⚽ KG: {kg}
📈 2.5: {over25}
🕐 İY 0.5: {ih}
"""

def main():
    matches = get_matches()

    sent = 0

    for match in matches[:5]:
        analysis = analyze_match(match)

        msg = format_msg(match, analysis)
        send_to_channel(msg)

        sent += 1
        if sent >= 3:
            break

if __name__ == "__main__":
    main()
