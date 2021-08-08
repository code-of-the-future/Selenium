# Imported relevant modules
from selenium import webdriver
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
time.sleep(5)

# Let's start filling in forms!
phone_or_email = driver.find_element_by_name('emailOrPhone')
phone_or_email.send_keys('abciaknfdkuhgakns@yahoo.com')
full_name = driver.find_element_by_name('fullName')
full_name.send_keys('Ellie')
username = driver.find_element_by_name('username')
username.send_keys('futurekajfuhgasjbk')
password = driver.find_element_by_name('password')
password.send_keys('hellolaihgskbfndvjabsgiuda')
password.submit()
