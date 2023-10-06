import time
import configparser
import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# Create an object of the ConfigParser
config = configparser.ConfigParser()

# Read in the config file with the sensitive information
config.read('config.ini')

email = config.get('credentials', 'email')
password = config.get('credentials', 'password')
websiteVisiting = "https://www.nike.com/ie/launch"
typing_delay = 0.25
# Create a Safari WebDriver
driver = selenium.webdriver.Safari()
# Maximize the Safari window
time.sleep(1)
driver.maximize_window()

time.sleep(2)

# Use the driver to automate Safari
# Open the Google website

driver.get(websiteVisiting)
driver.implicitly_wait(5)

def doCookies():

    try:
        time.sleep(2)
        # reject_cookies = driver.find_element(By.ID, "onetrust-reject-all-handler")
        accept_cookies = driver.find_element(By.CLASS_NAME, "ripple")  # find the accept cookies button
        # reject_cookies.click()
        accept_cookies.click() # Click the accept cookies button

    except NoSuchElementException:
        print("Element not found")
    try:
        login = driver.find_element(By.CLASS_NAME, "sc-6wpn76-1")

        login.click()

    except NoSuchElementException:
        print("Element not found")
def check_for_accept_cookies():
    try:
        accept_cookies = driver.find_element(By.CLASS_NAME, "ripple")
        return accept_cookies  # Return the element if found
    except NoSuchElementException:
        return None  # Return None if not found

# Check if the "accept cookies" element is present
accept_cookies_element = check_for_accept_cookies()

if accept_cookies_element is not None:
    # The "accept cookies" element is found, so call the function
    doCookies()
else:
    # The "accept cookies" element is not present
    print("Accept cookies element not found")

time.sleep(7)

initial_login = driver.find_element(By.CLASS_NAME, "join-log-in")
time.sleep(3)
initial_login.click()
try:
    enter_email = driver.find_element(By.ID, "username")

    enter_email.click()
    time.sleep(2)
    for char in email:
        enter_email.send_keys(char)
        time.sleep(typing_delay)

    time.sleep(2)

    continue_to_password = driver.find_element(By.CLASS_NAME, "ripple")
    time.sleep(1)
    continue_to_password.click()

    time.sleep(3)
    enter_password = driver.find_element(By.ID, "password")
    enter_password.click()
    for char in password:
        enter_password.send_keys(char)
        time.sleep(typing_delay)

    continue_to_sign = driver.find_element(By.CLASS_NAME, "ripple")
    continue_to_sign.click()


    def doPreferences():

        try:
            time.sleep(2)

            accept_preferences = driver.find_element(By.CLASS_NAME, "ripple")  # find the accept cookies button
            accept_preferences.click()  # Click the accept cookies button

        except NoSuchElementException:
            print("Element not found")



    def check_for_preferences():
        try:
            accept_preferences = driver.find_element(By.CLASS_NAME, "ripple")
            return accept_preferences  # Return the element if found
        except NoSuchElementException:
            return None  # Return None if not found


    # Check if the "preferences" element is present
    accept_preferences_element = check_for_preferences()

    if accept_preferences_element is not None:
        # The "preferences" element is found, so call the function
        doPreferences()
    else:
        # The "preferences" element is not present
        print("Accept cookies element not found")


except NoSuchElementException:
    print("element not found")
# Wait for a few seconds (e.g., 10 seconds) to keep the browser open
time.sleep(10)
# Close the browser
driver.quit()