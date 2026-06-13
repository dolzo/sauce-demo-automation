from selenium.webdriver.common.by import By

class Login:
    input_username = (By.XPATH, "//input[@id='user-name']")
    input_password = (By.XPATH, "//input[@id='password']")
    button_login = (By.XPATH, "//input[@id='login-button']")
    div_inventory_container = (By.XPATH, "//div[@id='inventory_container']")