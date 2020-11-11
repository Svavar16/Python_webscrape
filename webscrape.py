from selenium import webdriver
from bs4 import BeautifulSoup

# we need to tell selenium where the chromedrive is
# this is the location on my computer, it might be different on yours
chrome_loc = "/usr/bin/chromedriver" 

# then we tell the selenium where chromedriver is
driver = webdriver.Chrome(chrome_loc)

# you can use different browsers, I just like chrome
# then we get the webpage.
driver.get("somesite")

# then we get the content form this page
content = driver.page_source
# and then we parse the content
# html.parser tells the Beautiful soup that it's looking
# at a website, and will act acordingly
soup = BeautifulSoup(content, 'html.parser')