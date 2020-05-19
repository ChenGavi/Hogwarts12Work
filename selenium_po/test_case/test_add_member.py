from selenium_po.page.browser import Browser


class TestAddMember:

    def setup(self):
        self.main = Browser.start()

    def teardown(self):
        Browser.quit()

    def test_add_member(self):
        add_member = self.main.to_add_member()
        add_member.add_member()
        assert add_member.get_member("felix")