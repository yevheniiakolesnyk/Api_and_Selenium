import time
from selenium import webdriver

# get Google
driver = webdriver.Chrome()
driver.get('https://www.google.com.ua/')
driver.implicitly_wait(30)

# write script
script = "alert('Alert via Selenium')"

# wait for page to load
time.sleep(3)

# generate alert via JavaScript
driver.execute_script(script)

# switch to alert and accept it
alert = driver.switch_to.alert
alert.accept()
