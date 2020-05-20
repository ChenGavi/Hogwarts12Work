import shelve
from time import sleep

from selenium import webdriver
from selenium_po.page.main_page import MainPage


class Browser():
    _login_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"
    _main_url = "https://work.weixin.qq.com/wework_admin/frame"

    @classmethod
    def start(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(cls._login_url)

        db = shelve.open("cookies")
        cookies = db["cookie"]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            cls.driver.add_cookie(cookie)
        cls.driver.get(cls._main_url)

        if cls.driver.current_url != cls._main_url:
            # 手动扫码
            sleep(10)
            db["cookie"] = cls.driver.get_cookies()
        db.close()

        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()