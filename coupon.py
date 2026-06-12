def create_coupon(analyses):
    print("----- Kupon -----")
    for item in analyses:
        print(f"{item['match']} → Tahmin: {item['prediction']}, Güven: {item['confidence']}%")
    print("----------------")
