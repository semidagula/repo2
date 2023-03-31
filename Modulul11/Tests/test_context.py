import time

from Modulul11.Pages.context_page import CustomPage
from Modulul11.Tests.base_test import BaseTest


class ContextMenu(BaseTest):

    def test_4(self):
        page = CustomPage(self.driver)
        page.click_custom_button()
        page.right_click_hot_spot()
        time.sleep(3)
        page.accept_alert()
        time.sleep(3)
