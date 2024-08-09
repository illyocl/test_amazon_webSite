
from selenium.webdriver.common.by import By
import allure



class BackPage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step('False Test Step')
    def back_false(self):
        try:
            assert False, "Bu adım kasıtlı olarak başarısız olacak"
        except AssertionError as e:
            print("Test kasıtlı olarak başarısız oldu:", e)
            raise e






