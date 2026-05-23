from api import get_matches
from analyzer import analyze_match
from sender import send_to_channel

def format_match(match, a):
    home = match["teams"]["home"]["name"]
    away = match["teams"]["away"]["name"]

    return f"""
⚽ {home} - {away}

📊 MS: {a['ms']}
⚽ KG: {a['kg']}
📈 2.5: {a['over25']}
🕐 İY 0.5: {a['first_half']}
📊 Güven: %{a['confidence']}
"""

def main():
    matches = get_matches()

    kupon = []
    kupon_conf = 0

    for match in matches:

        a = analyze_match(match)

        # 🔥 filtre: sadece güçlü maçlar
        if a["confidence"] >= 60:
            kupon.append(format_match(match, a))
            kupon_conf += a["confidence"]

        if len(kupon) >= 3:
            break

    # kupon mesajı
    msg = "🔥 GÜNÜN KUPONU 🔥\n\n"
    msg += "\n".join(kupon)

    msg += f"\n\n📊 Ortalama Güven: %{kupon_conf // len(kupon) if kupon else 0}"

    send_to_channel(msg)

if __name__ == "__main__":
    main()
