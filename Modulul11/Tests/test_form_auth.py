import time
from Modulul11.Locators.form_auth_locators import FormAuth
from Modulul11.Pages.form_auth_page import FormAuthentication
from Modulul11.Pages.home_page import HomePage
from Modulul11.Tests.base_test import BaseTest


class TestFormAuth(BaseTest):
    def test_form_auth(self):
        form_page = FormAuthentication(self.driver)
        home = HomePage(self.driver)
        home.go_to_form_auth()
        form_page.go_to_pwd()
        user_name = self.driver.find_element(*FormAuth.USER)
        valid_user = 'tomsmith'
        user_name.send_keys(valid_user)
        password = self.driver.find_element(*FormAuth.PSW)
        valid_pwd = 'SuperSecretPassword!'
        password.send_keys(valid_pwd)
        form_page.login_btn()
        time.sleep(5)
        assert "/secure" in self.driver.current_url
        success_flash = self.driver.find_element(*FormAuth.SUCCESS_MSJ)
        assert success_flash.is_displayed()
        form_page.logout_btn()

