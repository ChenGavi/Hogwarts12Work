from selenium_po.page.browser import Browser


class TestAddMember:
    _expect_name = "9"

    def setup(self):
        self.main = Browser.start()

    def teardown(self):
        Browser.quit()

    def test_add_member(self):
        add_member = self.main.to_add_member()
        add_member.add_member()
        assert add_member.get_member(self._expect_name)
        add_member.delete_member()