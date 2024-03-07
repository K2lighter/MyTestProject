import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    Page_URL = Links.Login_page

    username_field = ('xpath', '//input[@name="username"]')
    password_field = ('xpath', '//input[@name="password"]')
    login_button = ('xpath', '//button[@type="submit"]')

    @allure.step("input username")
    def send_username(self, login):
        self.wait.until(EC.element_to_be_clickable(self.username_field)).send_keys(login)

    @allure.step("input password")
    def send_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.password_field)).send_keys(password)

    @allure.step("click login button")
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
