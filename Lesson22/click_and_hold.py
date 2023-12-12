import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://finsfera.ua')

slider = driver.find_element(By.XPATH, '//span[1]')
ActionChains(driver).click_and_hold(slider).move_by_offset(100, 0).release().perform()
ActionChains(driver).click_and_hold(slider).move_by_offset(50, 0).release().perform()

time.sleep(3)