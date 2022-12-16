import pytest
from selenium import webdriver
from selenium import webdriver
#chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    if request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.close()
