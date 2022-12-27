from Configs.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_HomePage(BaseTest):

    def test_home_page_title(self):
        self.login_Page = LoginPage(self.driver)
        homePage = self.login_Page.do_login(TestData.USER_ID, TestData.PASSWORD)
        homePage_title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert homePage_title == TestData.HOME_PAGE_TITLE

    def test_mngr_id(self):
        self.login_Page = LoginPage(self.driver)
        homePage = self.login_Page.do_login(TestData.USER_ID, TestData.PASSWORD)
        mngr_id = homePage.get_manager_id()
        assert mngr_id == TestData.MANAGER_ID