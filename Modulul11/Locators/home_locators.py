from selenium.webdriver.common.by import By


class HomeLocators:
    ALERT_JS = (By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
    CONTEXT_MENU = (By.XPATH, '#content > ul > li:nth-child(7) > a')
    FORM_AUTHENTICATION = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    CHECKBOXES = (By.XPATH, '//*[@id="content"]/ul/li[6]/a')
    BASIC_AUTH = (By.XPATH, '//*[@id="content"]/ul/li[3]/a')
    AB_TESTING = (By.XPATH, '//*[@id="content"]/ul/li[1]/a')
    ADD_REMOVE_ELEMENTS = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')
