from analyzer import analyze_match

def build_ticket(matches):

    all_list = []
    banko = []
    iy_list = []
    skor_list = []

    for m in matches:

        a = analyze_match(m)

        home = m["teams"]["home"]["name"]
        away = m["teams"]["away"]["name"]

        if a["prob"] < 70:
            continue

        text = f"""
⚽ {home} - {away}
📊 MS: {a['ms']}
⚽ KG: {a['kg']}
📈 2.5: {a['over25']}
🕐 İY: {a['iy']}
🎯 Value: {a['value']}%
"""

        all_list.append(text)

        if len(banko) < 4:
            banko.append(text)

        iy_list.append(f"{home}-{away} | İY: {a['iy']}")
        skor_list.append(f"{home}-{away} | MS: {a['ms']}")

    return {
        "all": all_list,
        "banko": banko,
        "iy": iy_list[:4],
        "skor": skor_list[:4]
    }
