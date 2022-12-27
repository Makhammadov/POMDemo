from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class HomePage(BasePage):
    MNGR_ID = (By.CSS_SELECTOR, "tr.heading3 td") #if does not work add td after class name

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def get_manager_id(self):
        return self.get_element_text(self.MNGR_ID)




