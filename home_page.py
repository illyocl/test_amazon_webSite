
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Accept cookies')
    def accept_cookies(self):
        try:
            accept_cookies_button = self.driver.find_element(By.NAME, "accept")
            accept_cookies_button.click()
            print("Çerez kabul butonu tıklandı.")
        except Exception as e:
            print("Çerez kabul butonu bulunamadı veya tıklanamadı:", e)


