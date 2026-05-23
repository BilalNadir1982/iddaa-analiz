from api import get_matches
from sender import send_to_channel

def main():
    matches = get_matches()

    if not matches:
        send_to_channel("Bugün maç bulunamadı.")
        return

    msg = "🔥 Günün İddaa Analizi 🔥\n\n"

    for match in matches[:3]:
        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]

        msg += f"⚽ {home} - {away}\n"
        msg += "💡 Tahmin: KG VAR\n\n"

    send_to_channel(msg)

if __name__ == "__main__":
    main()
