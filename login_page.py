
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from user import User

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Attempt invalid login with email')
    def invalid_login_email(self):
        login_page_button = self.driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
        login_page_button.click()
        login_page_email1 = self.driver.find_element(By.ID, "ap_email")
        login_page_email1.send_keys(User.invalid_email)
        login_page_email1.send_keys(Keys.RETURN)
        error_email = self.driver.find_element(By.XPATH, '//*[@id="auth-error-message-box"]/div/div/ul/li/span').text
        assert "Bu e-posta adresiyle bir hesap bulamıyoruz" in error_email
        print("Hatalı email girildi.")
        time.sleep(1)

    @allure.step('Login with valid email')
    def valid_login_email(self):
        login_page_email2 = self.driver.find_element(By.ID, "ap_email")
        login_page_email2.clear()
        login_page_email2.send_keys(User.valid_email)
        login_page_email2.send_keys(Keys.RETURN)
        time.sleep(1)

    @allure.step('Attempt invalid login with password')
    def invalid_login_password(self):
        login_page_password1 = self.driver.find_element(By.ID, "ap_password")
        login_page_password1.send_keys(User.invalid_password)
        login_page_password1.send_keys(Keys.RETURN)
        error_password = self.driver.find_element(By.XPATH, '//*[@id="auth-error-message-box"]/div/div/ul/li/span').text
        assert "Şifreniz yanlış" in error_password
        print("Hatalı şifre girildi.")
        time.sleep(1)

    @allure.step('Login with valid password')
    def valid_login_password(self):
        try:
            login_page_password2 = self.driver.find_element(By.ID, "ap_password")
            login_page_password2.clear()
            login_page_password2.send_keys(User.valid_password)
            login_page_password2.send_keys(Keys.RETURN)
            print("Doğru şifre ve email, giriş yapıldı.")
            time.sleep(1)
        except Exception as e:
            print("Giriş yapılamadı:", e)



