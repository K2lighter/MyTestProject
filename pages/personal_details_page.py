import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from config.links import Links
from time import sleep


class Personal(BasePage):
    Page_URL = Links.Personal_page
    first_name_field = ('xpath', '//input[@name="firstName"]')
    save_button = ('xpath', '//button[@type="submit"][1]')
    spinner = ('xpath', '//div[@class="oxd-loading-spinner-container"]')

    def enter_first_name(self, new_name):
        with allure.step(f"change name on '{new_name}'"):
            first_name_val = self.wait.until(EC.element_to_be_clickable(self.first_name_field))
            first_name_val.send_keys(Keys.CONTROL + "A")  # очистить поле
            first_name_val.send_keys(Keys.BACKSPACE)
            first_name_val.send_keys(new_name)
            self.name = new_name

    @allure.step("click save button")
    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    @allure.step("name has been matched")
    def check_changed_is_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.spinner))
        self.wait.until(EC.visibility_of_element_located(self.first_name_field))
        self.wait.until(EC.text_to_be_present_in_element_value(self.first_name_field, self.name))
