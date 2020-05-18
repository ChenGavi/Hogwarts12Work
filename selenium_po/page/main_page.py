import shelve
from time import sleep

from selenium.webdriver.common.by import By

from selenium_po.page.base_page import BasePage
from selenium_po.page.add_member import AddMember


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    _add_member_button = (By.CSS_SELECTOR,
                          ".index_service_cnt.js_service_list > a:nth-child(1) .index_service_cnt_item_title")

    def to_add_member(self):
        self.driver.get(self._base_url)
        sleep(10)
        db = shelve.open("cookies")
        db["cookie"] = self.driver.get_cookies()
        cookies = db["cookie"]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.find(self._add_member_button).click()
        return AddMember(self.driver)