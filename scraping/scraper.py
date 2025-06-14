from playwright.sync_api import sync_playwright

def fetch_chapter(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()
        page.goto(url)


        content = page.inner_text("div#mw-content-text")

        page.screenshot(path = 'chapter_1.png',full_page= True)
        browser.close()
        return content
    

if __name__ == "__main__":
    url = 'https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1'

    text = fetch_chapter(url)

    with open("chapter1.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("Chapter text and screenshot saved successfully!")
