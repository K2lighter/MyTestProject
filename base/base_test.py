import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from pages.personal_details_page import Personal


class BaseTest:
    data: Data
    login_page: LoginPage
    dashboard_page: Dashboard
    personal_page: Personal

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = Dashboard(driver)
        request.cls.personal_page = Personal(driver)

