import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigate to Url
driver = webdriver.Chrome()
driver.get('https://pythonexamples.org/tmp/selenium/index-29.html')

# Get the element
element = driver.find_element(By.ID, 'para4')
time.sleep(2)

# Scroll to the element using JavaScript
driver.execute_script('arguments[0].scrollIntoView();', element)
time.sleep(2)

# Close the driver
driver.quit()
