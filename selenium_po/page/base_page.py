from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = None

    def __init__(self, driver: webdriver):
        self.driver = driver

    def find(self, by_locator):
        return self.driver.find_element(*by_locator)

    def finds(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def send_text(self, by_locator, text):
        self.find(by_locator).send_keys(text)

    def wait_for_click(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))

    def wait_for_elememt(self, conditions, time=10):
        WebDriverWait(self.driver, time).until(conditions)