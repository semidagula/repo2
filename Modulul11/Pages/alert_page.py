from Modulul11.Locators.alerts_locators import AlertLocators


class AlertPage:
    def __init__(self, driver):
        self._driver = driver

    def page_confirm(self):
        self._driver.find_element(*AlertLocators.ALERT_JS_CONFIRM).click()

    def page_prompt(self):
        self._driver.find_element(*AlertLocators.ALERT_JS_PROMPT).click()

    def get_text_for_result(self):
        return self._driver.find_element(*AlertLocators.RESULT).text
