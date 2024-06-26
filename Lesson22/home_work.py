from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


def test_scroll():
    base_url = 'https://www.behance.net/gallery/18988225/B-Yoga-Website'
    driver = webdriver.Chrome()
    driver.get(base_url)
    like_icon = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div[1]/div[2]/main/div/div/div[1]/div/div[2]/div[2]/div[3]/div[1]/div/span/div')
    time.sleep(3)
    driver.execute_script('arguments[0].scrollIntoView();', like_icon)
    assert like_icon.is_enabled()
    driver.quit()


def test_scroll_and_click():
    base_url = 'https://www.behance.net/gallery/18988225/B-Yoga-Website'
    driver = webdriver.Chrome()
    driver.get(base_url)
    comment_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                               '/html/body/div[1]/div/div/div[1]/div[2]/main/div/div/div[1]/div/div[2]/div[2]/div[4]/div[2]/div/div[1]/div/div[2]')))
    driver.execute_script('arguments[0].scrollIntoView();', comment_link)
    driver.execute_script('arguments[0].click();', comment_link)
    comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                              '/html/body/div[1]/div/div/div[1]/div[2]/main/div/div/div[1]/div/div[2]/div[2]/div[4]/div[2]/div/div[1]/div/ul/li[13]/div/div[2]/div[2]')))
    # driver.execute_script('arguments[0].scrollIntoView();', comment)
    assert comment.is_enabled()
    driver.quit()


def test_scroll_up_and_down_click():
    base_url = 'https://www.behance.net/gallery/18988225/B-Yoga-Website'
    driver = webdriver.Chrome()
    driver.get(base_url)
    down_scroll = 2000
    driver.execute_script(f'window,scrollTo(0, {down_scroll})')
    up_scroll = 0
    driver.execute_script(f'window,scrollTo(0, {up_scroll})')
    allert_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/nav/div/div[2]/div[5]/div[1]/div')))
    action =ActionChains(driver)
    action.move_to_element(allert_icon).perform()
    notification = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"We looked back")]')))
    assert notification.is_enabled()
