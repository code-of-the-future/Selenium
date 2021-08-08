# Explicit and Implicit Waits
# Imported relevant modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a path
PATH = '/Users/elliesleightholm/Downloads/chromedriver'
# (On Windows: PATH = 'C:\chromedriver.exe')
# Create a driver
driver = webdriver.Chrome(PATH)
# Open a website
driver.get('https://www.instagram.com/accounts/emailsignup/')

# First of all, we need to accept the cookies:
cookies = driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]')
cookies.click()

# Implicit Wait
# driver.implicitly_wait(10)  # Waits for 10 seconds

# Explicit Wait
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "emailOrPhone"))
    )
finally:
    driver.quit()
