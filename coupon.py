```python
# coupon.py

# =========================================
# AUTO COUPON ENGINE
# =========================================

def create_coupon(matches):

    banko = []

    for match in matches:

        if match["score"] >= 85:
            banko.append(match)

    banko = sorted(
        banko,
        key=lambda x: x["score"],
        reverse=True
    )

    return banko[:3]
```
