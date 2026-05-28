def create_coupon(matches):

    banko = [m for m in matches if m["score"] >= 85]

    banko = sorted(banko, key=lambda x: x["score"], reverse=True)

    return banko[:3]
