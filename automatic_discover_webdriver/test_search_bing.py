import os
import sys
import pathlib
import pytest
from time import sleep
from selenium import webdriver

parent_dir = pathlib.Path.cwd().parent
sys.path.append(str(parent_dir))

class SearchBing:

    def setup(self):
        self.driver = webdriver.Chrome()
        pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_search_bing(self):
        self.driver.get("https://www2.bing.com/")
        self.driver.find_element_by_id("sb_form_q").send_keys("必应")
        self.driver.find_element_by_id("sb_form_go").click()
        sleep(3)


if __name__ == '__main__':
    pytest.main()