import time

import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

email = "michaelnjoku1200@gmail.com"
password = "Xtreme32"
typing_delay = 0.25
# Create a Safari WebDriver
driver = selenium.webdriver.Safari()

# Maximize the Safari window
driver.maximize_window()

# Use the driver to automate Safari
# Open the ticketmaster website
driver.get("https://www.ticketmaster.ie")
driver.implicitly_wait(5)

try:
    time.sleep(2)
    # reject_cookies = driver.find_element(By.ID, "onetrust-reject-all-handler")
    accept_cookies = driver.find_element(By.ID ,"onetrust-accept-btn-handler")
   # reject_cookies.click()
    accept_cookies.click()

except NoSuchElementException:
    print("Element not found")
try:
    login = driver.find_element(By.CLASS_NAME,"sc-6wpn76-1")

    login.click()

except NoSuchElementException:
    print("Element not found")

time.sleep(5)
try:
    enter_email = driver.find_element(By.ID, "email[objectobject]__input")

    enter_email.click()
    for char in email:
        enter_email.send_keys(char)
        time.sleep(typing_delay)


    time.sleep(2)
    enter_password = driver.find_element(By.ID,"password[objectobject]__input")
    enter_password.click()
    for char in password:
        enter_password.send_keys(char)
        time.sleep(typing_delay)



    time.sleep(2)
    remember_me = driver.find_element(By.CLASS_NAME,"sc-qYHkt")
    remember_me.click()
    time.sleep(4)
    sign_in = driver.find_element(By.NAME,"sign-in")
    sign_in.click()
except NoSuchElementException:
    print("element not found")
# Wait for a few seconds (e.g., 10 seconds) to keep the browser open
time.sleep(10)
# Close the browser
driver.quit()