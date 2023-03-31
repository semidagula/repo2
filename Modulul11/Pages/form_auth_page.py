from Modulul11.Locators.form_auth_locators import FormAuth


class FormAuthentication:
    def __init__(self, driver):
        self._driver = driver

    def go_to_user(self):
        self._driver.find_element(*FormAuth.USER).click()

    def go_to_pwd(self):
        self._driver.find_element(*FormAuth.PSW).click()

    def login_btn(self):
        self._driver.find_element(*FormAuth.LOGIN_BTN).click()

    def secure_area(self):
        return self._driver.find_element(*FormAuth.SECURE_AREA)

    def logout_btn(self):
        self._driver.find_element(*FormAuth.LOGOUT_BTN).click()

    def succes_msj(self):
        self._driver.find_element(*FormAuth.SUCCES_MSJ)