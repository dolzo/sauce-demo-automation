from .base_actions import BaseActions
from pages.page_objects.login import Login

#TODO: Quitar esta importacion, ahora esta activa solo como guia para el intellisense
from selenium.webdriver.chrome.webdriver import WebDriver

class LoginActions(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    def type_username(self, username:str):
        self.type_info(Login.input_username, username)

    def type_password(self, password:str):
        self.type_info(Login.input_password, password)

    def click_submit_button(self):
        self.click_on_element(Login.button_login)

    def user_is_logged(self) -> bool:
        return self.is_displayed(Login.div_inventory_container)