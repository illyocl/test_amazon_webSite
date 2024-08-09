import allure
from selenium.webdriver.common.by import By
import time


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Go to cart')
    def go_to_cart(self):
        try:
            go_to = self.driver.find_element(By.XPATH, '//*[@id="nav-cart"]')
            go_to.click()
            print("Sepete gidildi.")

            # Ekran görüntüsünü kaydetme
            screenshot_path = "./sepetgoruntusu.png"
            self.driver.save_screenshot(screenshot_path)

            # Allure raporuna ekran görüntüsünü ekleme
            allure.attach.file(screenshot_path, name="Sepet Görüntüsü", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            print("Sepete gidilemedi:", e)

    @allure.step('Decrease product quantity')
    def decrease_quantity(self):
        try:
            dropdown = self.driver.find_element(By.XPATH, '//*[@id="a-autoid-0-announce"]')
            dropdown.click()
            time.sleep(1)
            decrease_to = self.driver.find_element(By.ID, "quantity_1")
            decrease_to.click()
            print("Ürün adedi azaltıldı.")
        except Exception as e:
            print("Ürün azaltılamadı:", e)

    @allure.step('Complete shopping')
    def complete_shopping(self):
        try:
            complete_shop = self.driver.find_element(By.NAME, "proceedToRetailCheckout")
            complete_shop.click()
            print("Alışveriş bitirildi.")
        except Exception as e:
            print("Alışveriş bitirilemedi:", e)



