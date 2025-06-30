import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Headless = Kein Fenster sichtbar
        page = await browser.new_page()
        await page.goto('https://webscraper.io/test-sites/e-commerce/allinone')

        title = await page.title()

        preis_element = await page.query_selector('span[itemprop="price"]')
        preis = await preis_element.text_content()

        preis_elemente = await page.query_selector_all('span[itemprop="price"]')
        #print(preis_elemente) [<JSHandle preview=JSHandle@node>, <JSHandle preview=JSHandle@node>, <JSHandle preview=JSHandle@node>]
        # Texte extrahieren
        for i, element in enumerate(preis_elemente, start=1):
            text = await element.text_content()
            print(f"Preis {i}: {text}")

        print(f"Seitentitel: {title}")
        print(f"Preis: {preis}")
        await browser.close()

asyncio.run(main())
