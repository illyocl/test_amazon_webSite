
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Search product: {product_name}')
    def search_product(self, product_name):
        try:
            search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
            search_box.send_keys(product_name)
            search_box.send_keys(Keys.RETURN)
            print("Arama butonu tıklandı.")
        except Exception as e:
            print("Arama butonu bulunamadı veya tıklanamadı:", e)

    @allure.step('Find brand')
    def find_brand(self):
        try:
            self.driver.execute_script("window.scrollBy(0,300)", "")
            select_brand = self.driver.find_element(By.XPATH, '//*[@id="p_123/110955"]/span/a/div/label/i')
            select_brand.click()
            print("Marka seçildi.")
        except Exception as e:
            print("Marka seçilemedi:", e)

    @allure.step('Select product')
    def select_product(self):
        try:
            product = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[10]/div/div/span/div/div/div[2]/div[2]/h2/a/span'))
            )
            product.click()
            print("Ürün seçildi.")
        except Exception as e:
            print("Ürün seçilemedi:", e)


