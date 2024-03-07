import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from config.links import Links


class Dashboard(BasePage):
    Page_URL = Links.Dashboard_page
    my_info_field = ('xpath', '//span[text()="My Info"]')

    @allure.step("click my info")
    def click_my_info(self):
        self.wait.until(EC.element_to_be_clickable(self.my_info_field)).click()
