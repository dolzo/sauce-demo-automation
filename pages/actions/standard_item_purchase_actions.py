from .base_actions import BaseActions
from pages.page_objects.standard_item_purchase import standardItemPurchase

#TODO: Quitar esta importacion, ahora esta activa solo como guia para el intellisense
from selenium.webdriver.chrome.webdriver import WebDriver

class standardItemPurchaseActions(BaseActions):
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def click_backpack_add_to_cart_button(self):
        self.click_on_element(standardItemPurchase.button_add_backpack_to_cart)

    def click_cart_button(self):
        self.click_on_element(standardItemPurchase.button_shopping_cart)

    def click_checkout_button(self):
        self.click_on_element(standardItemPurchase.button_checkout)

    def type_first_name(self, first_name:str):
        self.type_info(standardItemPurchase.input_first_name, first_name)

    def type_last_name(self, last_name:str):
        self.type_info(standardItemPurchase.input_last_name, last_name)

    def type_postal_code(self, postal_code:str):
        self.type_info(standardItemPurchase.input_postal_code, postal_code)

    def click_continue_to_checkout_overview(self):
        self.click_on_element(standardItemPurchase.button_continue)

    def click_finish_button(self):
        self.click_on_element(standardItemPurchase.button_finish)

    def item_was_purchased(self) -> bool:
        return self.is_displayed(standardItemPurchase.div_order_completed)