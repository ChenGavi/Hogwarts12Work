from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import By


class TestDemo:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        caps["skipServerInstallation"] = True
        caps["skipDeviceInitialization"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        pass
        # self.driver.close()

    # 参数化
    @pytest.mark.parametrize("keyword,text,add_text,expect_text",[
        ("alibaba", "BABA", "加自选", "已添加"),
        ("jd", "JD", "加自选", "已添加"),
        ("xiaomi", "01810", "加自选", "已添加")
    ])
    def test_search(self, keyword, text, add_text, expect_text):
        self.driver.find_element(By.ID, "home_search").click()
        self.driver.find_element(By.ID, "search_input_text").send_keys(keyword)
        sleep(1)
        self.driver.find_element(By.XPATH, f"//*[@text='{text}']").click()
        self.driver.find_element(By.XPATH, f"//*[@text='{add_text}']").click()

        # 断言
        ele_text = self.driver.find_element(By.ID, "followed_btn").text
        assert ele_text == expect_text

