import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to Url
driver = webdriver.Chrome()
driver.get('https://www.awwwards.com/sites/23bis')

# Locate the 'Accept Cookie' button
try:
    # Find the button by text using XPATH
    wait = WebDriverWait(driver, 30)
    accept_cookie_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Accept Cookies")]')))
except:
    # If not found by text, find by class name
    try:
        accept_cookie_button = driver.find_element(By.CLASS_NAME, 'button button--medium--rounded--extra--pad')
    except:
        # If not found by any method, raise the exception
        raise Exception('Unable to find "Accept Cookies" button')

# Click the button to accept cookies
accept_cookie_button.click()
time.sleep(3)

# Scroll
scroll_pause = 3

# Get scroll height
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    # Scroll down to bottom
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # Wait to load the page
    time.sleep(scroll_pause)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height


# Close the driver
driver.quit()
