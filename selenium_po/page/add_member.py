from selenium.webdriver.common.by import By
from selenium_po.page.base_page import BasePage


class AddMember(BasePage):
    _username_locator = (By.ID,"username")
    _username = "9"
    _member_acctid_locator = (By.ID,"memberAdd_acctid")
    _member_acctid = "99"
    _member_phone_locator = (By.ID, "memberAdd_phone")
    _member_phone = "11011001188"
    _btn_save_locator = (By.CSS_SELECTOR, ".js_btn_save")

    _member_table_locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_tr td:nth-child(2)")
    _page_info_locator = (By.CSS_SELECTOR, ".ww_pageNav_info_text")
    _next_page_locator = (By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal")

    _member_search_locator = (By.ID, "memberSearchInput")
    _member_delete_locator = (By.CSS_SELECTOR, ".js_del_member")
    _que_btn_locator = (By.CSS_SELECTOR, ".ww_dialog_foot .ww_btn_Blue")

    def add_member(self):
        self.send_text(self._username_locator, self._username)
        self.send_text(self._member_acctid_locator, self._member_acctid)
        self.send_text(self._member_phone_locator, self._member_phone)
        self.find(self._btn_save_locator).click()

    def update_page(self):
        content = self.find(self._page_info_locator).text
        return [int(x) for x in content.split('/', 1)]

    def get_member(self, value):
        cur_page, total_page = self.update_page()

        while True:
            elements = self.finds(self._member_table_locator)
            for element in elements:
                if value == element.text:
                    return True

            if cur_page == total_page:
                return False

            cur_page = self.update_page()[0]
            self.find(self._next_page_locator).click()

    def delete_member(self):
        self.send_text(self._member_search_locator, self._username)
        self.wait_for_find(self._member_delete_locator).click()
        self.wait_for_find(self._que_btn_locator).click()
