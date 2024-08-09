
import time

from selenium import webdriver
import chromedriver_autoinstaller

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def setup_class(cls):
        chromedriver_autoinstaller.install()
        cls.driver = webdriver.Chrome()
        #cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        time.sleep(2)



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


