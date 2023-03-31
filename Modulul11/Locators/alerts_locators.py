from selenium.webdriver.common.by import By


class AlertLocators:

    ALERT_JS_CONFIRM = (By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
    ALERT_JS_PROMPT = (By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
    RESULT = (By.ID, 'result')
