from db import init_db, already_sent, mark_sent
from sender import send_to_channel
from analyzer import generate_analysis

def main():
    init_db()

    if already_sent():
        print("⚠️ Bugün zaten gönderildi")
        return

    msg = generate_analysis()

    send_to_channel(msg)
    mark_sent()

    print("✅ Analiz gönderildi")

if __name__ == "__main__":
    main()
