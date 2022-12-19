from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Configs.config import TestData

class LoginPage(BasePage):
    USER_ID_TEXTBOX= (By.NAME, "uid")
    PASSWORD_TEXTBOX = (By.NAME, "password")
    LOGIN_BTN = (By.NAME, "btnLogin")
    def __init__ (self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    def get_login_page_title(self, title):
         return self.get_title(title)
    def do_login(self, username, password):
        self.do_send_keys(self.USER_ID_TEXTBOX, username)
        self.do_send_keys(self.PASSWORD_TEXTBOX, password)
        self.do_click(self.LOGIN_BTN)






