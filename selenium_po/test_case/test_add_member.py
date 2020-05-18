from selenium_po.page.main_page import MainPage
from selenium_po.page.add_member import AddMember


class TestAddMember:

    def setup(self):
        self.main = MainPage()

    def test_add_member(self):
        add_member = self.main.to_add_member()
        add_member.add_member()
        assert "felix" in add_member.get_member("add_member")
        add_member.delete_member()