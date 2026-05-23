from api import get_matches
from signal import build_ticket
from sender import send_to_channel

def main():

    matches = get_matches()

if not matches:
    send_to_channel("❌ BUGÜN MAÇ VERİSİ YOK (API boş döndü)")

    tickets = build_ticket(matches)

    if tickets["all"]:
        send_to_channel("🔥 GENEL KUPON 🔥\n\n" + "\n".join(tickets["all"]))

    if tickets["banko"]:
        send_to_channel("💣 BANKO KUPON 🔥\n\n" + "\n".join(tickets["banko"]))

    if tickets["iy"]:
        send_to_channel("🕐 İY MS KUPONU 🔥\n\n" + "\n".join(tickets["iy"]))

    if tickets["skor"]:
        send_to_channel("🎯 SKOR KUPONU 🔥\n\n" + "\n".join(tickets["skor"]))


if __name__ == "__main__":
    main()
