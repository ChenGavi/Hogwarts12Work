from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def __init__(self, driver: webdriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver
        self.driver.maximize_window()

    def find(self, by_locator):
        return self.driver.find_element(*by_locator)

    def finds(self, by_locator):
        return self.driver.find_element(*by_locator)

    def send_text(self, by_locator, text):
        self.driver.find_element(*by_locator).send_keys(text)

    def wait_find_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))