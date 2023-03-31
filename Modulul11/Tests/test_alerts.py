import time

from Modulul11.Pages.alert_page import AlertPage
from Modulul11.Pages.home_page import HomePage
from Modulul11.Tests.base_test import BaseTest


class TestAlerts(BaseTest):

    def test_3(self):
        home_page = HomePage(self.driver)
        alert_page = AlertPage(self.driver)
        actiuni = self.driver.switch_to.alert
        actiuni.accept()
        home_page.go_to_alert_section()
        alert_page.page_prompt()
        actiuni.dismiss()
        alert_page.page_confirm()
        my_input = 'hehe'
        actiuni.send_keys(my_input)
        actiuni.click_to_accept()
        assert my_input in alert_page.get_text_for_result()
        time.sleep(3)
