from time import sleep
from selenium.webdriver.common.by import By

from selenium_po.page.base_page import BasePage
from selenium_po.page.add_member import AddMember


class MainPage(BasePage):
    _add_member_button = (By.CSS_SELECTOR,
                          ".index_service_cnt.js_service_list > a:nth-child(1) .index_service_cnt_item_title")

    def to_add_member(self):
        # 显示等待
        # self.wait_for_click(self._add_member_button).click()
        def wait_add_member(x):
            element_len = len(self.finds(self._add_member_button))
            if element_len > 0:
                print("121212")
                self.find(self._add_member_button).click()
            return element_len > 0
        self.wait_for_elememt(wait_add_member)
        return AddMember(self.driver)