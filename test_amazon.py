
import time
import datetime
import unittest
import allure
import os

from base_page import BasePage
from home_page import HomePage
from login_page import LoginPage
from order_page import OrderPage
from order_detail_page import OrderDetailPage
from cart_page import CartPage
from back_page import BackPage

class AmazonTests(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)


    @classmethod
    def setUpClass(cls):
        BasePage.setup_class()
        cls.driver = BasePage.driver
        cls.driver.get("https://www.amazon.com.tr/")
        time.sleep(1)
        cls.homePage = HomePage(cls.driver)
        cls.loginPage = LoginPage(cls.driver)
        cls.orderPage = OrderPage(cls.driver)
        cls.orderDetailPage = OrderDetailPage(cls.driver)
        cls.cartPage = CartPage(cls.driver)
        cls.backPage = BackPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        BasePage.teardown_class()

    @allure.step('Home Page Test')
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_home_page(self):
        self.homePage.accept_cookies()

    @allure.step('Login Test')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_login(self):
        self.loginPage.invalid_login_email()
        self.loginPage.valid_login_email()
        self.loginPage.invalid_login_password()
        self.loginPage.valid_login_password()

    @allure.step('Order Test')
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_order(self):
        self.orderPage.search_product("macbook air m3")
        self.orderPage.find_brand()
        self.orderPage.select_product()

    @allure.step('Order Detail Test')
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_order_detail(self):
        self.orderDetailPage.increase_quantity()
        self.orderDetailPage.add_to_cart()

    @allure.step('Cart Test')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_05_cart(self):
        self.cartPage.go_to_cart()
        self.cartPage.decrease_quantity()
        self.cartPage.complete_shopping()


    @allure.step('False Test')
    @allure.severity(allure.severity_level.MINOR)
    def test_06_back(self):
        self.backPage.back_false()


if __name__ == '__main__':
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Jenkins iş alanına kaydet
    workspace = os.environ.get('WORKSPACE', os.getcwd())
    result_file = os.path.join(workspace, f"test_results_{now}.txt")

    with open(result_file, "w") as f:
        runner = unittest.TextTestRunner(stream=f)
        test_suite = unittest.TestLoader().loadTestsFromTestCase(AmazonTests)
        runner.run(test_suite)

    print(f"Test sonuçları '{result_file}' dosyasına kaydedildi.")

