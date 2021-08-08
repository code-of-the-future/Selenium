# Selenium Tutorial 1 & 2

# Importing the relevant modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a path
PATH = '/Users/elliesleightholm/Downloads/chromedriver'
# (On Windows: PATH = 'C:\chromedriver.exe')
# Create a driver
driver = webdriver.Chrome(PATH)
# Open a website
driver.get('https://www.google.com')
# Let's leave a bit of time for google before it closes
# time.sleep(5)
# This quits the web browser
# driver.quit()
# Close a specific tab
# driver.close()

# Let's start interacting with websites!

# First, we need to agree to the terms and conditions
agree = driver.find_element_by_id('L2AGLb')
agree.click()

# Clicking the search bar
element_search_bar = driver.find_element_by_name('q')
element_search_bar.click()

# We want to write something in the search bar
element_search_bar.send_keys('hello')
# You can press enter one of two ways
# element_search_bar.submit()
element_search_bar.send_keys(Keys.RETURN)  # ENTER or RETURN

# Introduction to Web Scraping
hello_text = driver.find_element_by_id('kp-wp-tab-overview')
print(hello_text.text)
