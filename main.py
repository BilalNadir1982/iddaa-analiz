from api import get_matches
from signal import generate_signal
from sender import send_to_channel

def main():
    matches = get_matches()

    sent = 0

    for match in matches:
        msg = generate_signal(match)

        if msg:
            send_to_channel(msg)
            sent += 1

        if sent >= 3:
            break

if __name__ == "__main__":
    main()
