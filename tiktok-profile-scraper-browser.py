from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    print('connecting...');
    browser = p.chromium.connect_over_cdp('https://<your-scraping-browser-username>:<your-scraping-browser-password>@<your-scraping-browser-host>', timeout=30000000)
    print('connected successfully');
    page = browser.new_page()
    print('navigating to the new page...')

    page.goto('https://www.tiktok.com/@tiktok', timeout=30000000)

    # wait until the page is loaded
    page.wait_for_selector('[data-e2e="following-count"]', timeout=30000000)

    html = page.content()

    soup = BeautifulSoup(html, 'html.parser')

    username = soup.find('h1', { 'data-e2e': 'user-title'}).text
    following = soup.find('strong', { 'data-e2e': 'following-count'}).text
    followers = soup.find('strong', { 'data-e2e': 'followers-count'}).text
    likes = soup.find('strong', { 'data-e2e': 'likes-count'}).text

    print('Username: ', username)
    print('Following: ', following)
    print('Followers: ', followers)
    print('Likes: ', likes)
