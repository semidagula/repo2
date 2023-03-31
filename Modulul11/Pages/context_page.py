from selenium.webdriver import ActionChains

from Modulul11.Locators.context_locators import ContextLocators
from Modulul11.Locators.home_locators import HomeLocators


class CustomPage:
    def __init__(self, driver):
        self._driver = driver

    def click_custom_button(self):
        self._driver.find_element(*HomeLocators.CONTEXT_MENU).click()

    def right_click_hot_spot(self):
        ac = ActionChains(self._driver)
        ac.context_click(self._driver.find_element(*ContextLocators.hot_spot)).perform()


