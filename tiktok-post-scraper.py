from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

with sync_playwright() as p:
 browser = p.chromium.launch(headless=False, slow_mo=50)
 page = browser.new_page()
 page.goto('https://www.tiktok.com/@tiktok/video/7263132423121046826', timeout=30000000)

 # wait until the page is loaded
 page.wait_for_selector('[data-e2e="comment-level-1"]', timeout=30000000)

 # Scroll the page for 5 seconds to load several comments
 start_time = time.time() # captures the current time
 while time.time() - start_time < 5: # run as long as the time elapsed since start_time is less than 5 seconds
   page.evaluate('window.scrollBy(0, window.innerHeight);') # scroll the webpage vertically by an amount equal to the height of the visible browser window
   time.sleep(2)  # introduces a delay of 1 second between each scroll operation

 html = page.content()

 soup = BeautifulSoup(html, 'html.parser')

 image = soup.select_one('[class*=ImgPoster]')['src']
 username = soup.find('span', { 'data-e2e': 'browse-username'}).text
 post_description = soup.select_one('[data-e2e=browse-video-desc]').find('span').text
 total_number_of_comments = soup.select_one('[class*=PCommentTitle]').text
 scraped_comments = soup.select('[data-e2e="comment-level-1"]')

 print('Video thumbnail link: ', image)
 print('Username: ', username)
 print('Video description: ', post_description)
 print('Total number of comments: ', total_number_of_comments)
 print('Number of scraped comments: ', len(scraped_comments))

 print('-------------------------------------------------------')
 print('The scraped comments:')
 for comment in scraped_comments:
   span = comment.find('span')
   if span:
     text = span.get_text()
     print(text)
