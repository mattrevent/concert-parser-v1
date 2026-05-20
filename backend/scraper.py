import asyncio
from playwright.sync_api import sync_playwright


def scrape_kassir(artist_name: str):
    results = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()

        url = f"https://kassir.ru/search#q={artist_name}&category=concert"
        page.goto(url, wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(2000)

        cards = page.query_selector_all("article.event-card")
        print(f"Найдено карточек: {len(cards)}")

        for card in cards:
            city = card.query_selector("[class*='city'], [class*='location']")
            date = card.query_selector("[class*='date'], time")
            price = card.query_selector("[class*='price']")

            results.append({
                "artist_name": artist_name,
                "city": city.inner_text() if city else "",
                "event_date": date.inner_text() if date else "",
                "min_price": price.inner_text() if price else "",
            })

        browser.close()

    return results

