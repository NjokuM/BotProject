import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Create a Safari WebDriver
driver = selenium.webdriver.Safari()

# Use the driver to automate Safari
# Open the Nike website
driver.get("https://www.nike.com")
driver.implicitly_wait(5)


try:
    wait = WebDriverWait(driver, 15)
    accept_all_cookies_button = driver.find_element(By.CSS_SELECTOR, ".nds-btn.dialog-actions-accept-btn.btn-primary-dark.btn-md")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nds-btn.dialog-actions-accept-btn.btn-primary-dark.btn-md")))
    accept_all_cookies_button.click()

    # Find the search bar element, wait 20 seconds for the search bar element to be clickable

    search_bar = driver.find_element(By.CLASS_NAME, "pre-search-btn")

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pre-search-btn")))

    search_bar.click()

    input_box = driver.find_element(By.ID, "VisualSearchInput")

    # Send keys to the search bar
    search_bar.send_keys("air force 1")

    # Submit the search query (press Enter)
    search_bar.send_keys(Keys.RETURN)

except NoSuchElementException:
    # Handle the case where the button is not found
    print("Button not found. Performing alternative action or error handling.")

# Close the browser
driver.quit()