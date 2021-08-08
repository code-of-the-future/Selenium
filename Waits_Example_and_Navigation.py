# Waits Example and Navigation
# Imported relevant modules
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a path
PATH = '/Users/elliesleightholm/Downloads/chromedriver'
# (On Windows: PATH = 'C:\chromedriver.exe')
# Create a driver
driver = webdriver.Chrome(PATH)
# Open a website
driver.get('https://www.google.com/')

# Launch google, locate the search bar, search for something,
# visit the first page and then do some navigating

# First, we need to agree to the terms and conditions
agree = driver.find_element_by_id('L2AGLb')
agree.click()

# Clicking the search bar
element_search_bar = driver.find_element_by_name('q')
element_search_bar.click()

# We want to write something in the search bar
element_search_bar.send_keys('Code of the future python youtube')
# You can press enter one of two ways
# element_search_bar.submit()
element_search_bar.send_keys(Keys.RETURN)  # ENTER or RETURN

# Explicit Wait
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/a'))
    )
    element.click()
    agree = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button')))
    agree.click()

    # Navigating
    driver.back()
    driver.forward()
    driver.clear()  # clear text
except:
    driver.quit()


