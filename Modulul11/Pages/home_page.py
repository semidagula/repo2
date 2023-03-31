from Modulul11.Locators.home_locators import HomeLocators


class HomePage:
    def __init__(self, driver):
        self._driver = driver

    def go_to_alert_section(self):
        self._driver.find_element(*HomeLocators.ALERT_JS).click()

    def go_to_context_menu(self):
        self._driver.find_element(*HomeLocators.CONTEXT_MENU).click()

    def go_to_form_auth(self):
        self._driver.find_element(*HomeLocators.FORM_AUTHENTICATION).click()

    def go_to_basic_auth(self):
        self._driver.find_element(*HomeLocators.BASIC_AUTH).click()

    def go_to_add_remove_elements(self):
        self._driver.find_element(*HomeLocators.ADD_REMOVE_ELEMENTS).click()

    def go_to_ab_testing(self):
        self._driver.find_element(*HomeLocators.AB_TESTING).click()
