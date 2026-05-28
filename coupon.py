def create_coupon(matches):

    banko = []

    for m in matches:
        if m["score"] >= 85:
            banko.append(m)

    return banko[:3]
