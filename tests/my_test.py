import random

import pytest
import allure

from base.base_test import BaseTest


@allure.feature("functional testing")
class TestStand(BaseTest):

    @allure.title("change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_name(self):
        self.login_page.open()
        self.login_page.send_username(self.data.Login)
        self.login_page.send_password(self.data.Password)
        self.login_page.click_login_button()

        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()

        self.personal_page.is_opened()
        self.personal_page.enter_first_name(f"user_test{random.randint(1, 100)}")
        self.personal_page.check_changed_is_saved()
        self.personal_page.screenshot("success")
