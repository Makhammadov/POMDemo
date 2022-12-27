from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Configs.config import TestData
class Test_Login(BaseTest):
    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_ID, TestData.PASSWORD)
