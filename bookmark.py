from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

def extract_urls(file_path, keyword):
    """Extract URLs containing the keyword from the bookmarks HTML file."""
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        anchors = soup.find_all("a")
        urls = [a["href"] for a in anchors if keyword in a["href"]]
    return urls

def open_urls(urls):
    """Open a list of URLs in new browser tabs."""
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    for url in urls:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(url)
        # time.sleep(2)  # Commented out or reduce the delay

    return driver

def main():
    file_path = "./bookmarks_7_24_24.html"
    keyword_youtube = "youtube.com"
    keyword_udemy = "udemy.com"

    # Extract YouTube URLs
    youtube_urls = extract_urls(file_path, keyword_youtube)
    print("Opening YouTube URLs...")
    driver = open_urls(youtube_urls)

    # Extract Udemy URLs
    udemy_urls = extract_urls(file_path, keyword_udemy)
    print("Opening Udemy URLs...")
    driver = open_urls(udemy_urls)

    # Keep the browser open indefinitely
    try:
        print("Browser will stay open. Press Ctrl+C to close.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
