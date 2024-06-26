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

# Scroll down and up
Y_1 = 2000
driver.execute_script(f'window,scrollTo(0, {Y_1})')
Y_2 = 0
driver.execute_script(f'window,scrollTo(0, {Y_2})')

# Close the driver
driver.quit()
