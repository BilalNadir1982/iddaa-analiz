from scraper import get_today_matches
from analyzer import analyze_matches
from coupon import create_coupon

def main():
    matches = get_today_matches()
    if not matches:
        print("Bugün maç bulunamadı.")
        return

    analyses = analyze_matches(matches)
    create_coupon(analyses)

if __name__ == "__main__":
    main()
