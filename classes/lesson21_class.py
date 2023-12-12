from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MySelenium:

    def __init__(self, browser_type="chrome"):
        self.browser_type = browser_type
        self.driver = self._get_driver()

    def _get_driver(self):
        if self.browser_type == 'chrome':
            driver = webdriver.Chrome()
        else:
            raise ValueError(f'Unsupported browser type: {self.browser_type}')
        return driver

    def get_page(self, url):
        self.driver.get(url)

    def search_box(self, my_text):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'APjFqb')))
        element.clear()
        element.send_keys(my_text)
        print(element.text)
        return my_text

    def redirect(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'APjFqb')))
        element.clear()
        element.send_keys('deepl')
        element.send_keys(Keys.RETURN)
        return self.driver.current_url

    def get_current_url(self):
        return self.driver.current_url

    def close_browser(self):
        return self.driver.quit()

    def go_through_links(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'a')))
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        links_list = []
        for lnk in links:
            lnk_to_switch = lnk.get_attribute('href')
            links_list.append(lnk_to_switch)
        for items in links_list:
            self.driver.get(items)
            self.driver.back()
        return self.driver.current_url
