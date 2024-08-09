
import allure
from selenium.webdriver.common.by import By
import time

class OrderDetailPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Increase product quantity')
    def increase_quantity(self):
        try:
            self.driver.execute_script("window.scrollBy(0,300)", "")
            piece = self.driver.find_element(By.XPATH, '//*[@id="a-autoid-0-announce"]')
            piece.click()
            increase_piece = self.driver.find_element(By.ID, "quantity_1")
            increase_piece.click()
            print("Ürün sayısı arttırıldı.")
            time.sleep(1)
        except Exception as e:
            print("Ürün sayısı arttırılamadı:", e)

    @allure.step('Add product to cart')
    def add_to_cart(self):
        try:
            add = self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]')
            add.click()
            print("Sepete eklendi.")
        except Exception as e:
            print("Sepete eklenemedi:", e)







