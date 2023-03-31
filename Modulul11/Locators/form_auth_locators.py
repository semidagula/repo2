from selenium.webdriver.common.by import By


class FormAuth:
    USER = (By.XPATH, '//*[@id="username"]')
    PSW = (By.XPATH, '//*[@id="password"]')
    LOGIN_BTN = (By.XPATH, '//*[@id="login"]/button/i')
    SECURE_AREA = (By.CSS_SELECTOR, '#flash')
    LOGOUT_BTN = (By.XPATH, '//*[@id="content"]/div/a')
    SUCCESS_MSJ = (By.CLASS_NAME, "flash.success")