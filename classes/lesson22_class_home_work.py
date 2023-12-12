from selenium import webdriver
import requests


class Image:

    def __init__(self, browser_type="chrome"):
        self.browser_type = browser_type
        self.driver = self._get_driver()

    def _get_driver(self):
        if self.browser_type == 'chrome':
            driver = webdriver.Chrome()
        else:
            raise ValueError(f'Unsupported browser type: {self.browser_type}')
        return driver

    def get_image(self, my_uri=''):
        url = "https://httpbin.org/image" + my_uri
        payload = {}
        headers = {
            'Accept': 'image/webp'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)
        return response.status_code
