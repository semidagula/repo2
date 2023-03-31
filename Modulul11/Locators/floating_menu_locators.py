from selenium.webdriver.common.by import By


class FloatingMenu:
    HOME = (By.XPATH, '//*[@id="menu"]/ul/li[1]/a')
    NEWS = (By.XPATH, '//*[@id="menu"]/ul/li[2]/a')
    CONTACT = (By.XPATH, '//*[@id="menu"]/ul/li[3]/a')
    ABOUT = (By.XPATH, '//*[@id="menu"]/ul/li[4]/a')
