from api import get_odds
from signal import build_ticket
from sender import send_to_channel

def main():

    matches = get_odds()

    tickets = build_ticket(matches)

    send_to_channel("🔥 GENEL VALUE KUPON 🔥\n\n" + "\n".join(tickets["all"]))

    send_to_channel("💣 BANKO KUPON 🔥\n\n" + "\n".join(tickets["banko"]))

    send_to_channel("🕐 İY MS KUPONU 🔥\n\n" + "\n".join(tickets["iy"]))

    send_to_channel("🎯 SKOR KUPONU 🔥\n\n" + "\n".join(tickets["skor"]))


if __name__ == "__main__":
    main()
