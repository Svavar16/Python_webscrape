from selenium import webdriver
from bs4 import BeautifulSoup

# we need to tell selenium where the chromedrive is
# this is the location on my computer, it might be different on yours
chrome_loc = "/usr/bin/chromedriver" 

# then we tell the selenium where chromedriver is
driver = webdriver.Chrome(chrome_loc)

# you can use different browsers, I just like chrome
# then we get the webpage.
driver.get("https://www.artstation.com/?sort_by=trending&dimension=2d")

# then we get the content form this page
content = driver.page_source
# and then we parse the content
# html.parser tells the Beautiful soup that it's looking
# at a website, and will act acordingly
soup = BeautifulSoup(content, 'html.parser')

# where we will then store the images
image = []
# then we will loop through the soup and see if we find what we are looking for
for a in soup.find_all('div', attrs={'class': 'gallery-grid'}):
    images = a.find_all('img', attrs={'class': 'd-block'})
    for item in images:
        image.append(item['src'])

# then we loop through and print out the item in the array
for item in image:
    print(item)

# and then we close the selenium, or it's driver
driver.close()