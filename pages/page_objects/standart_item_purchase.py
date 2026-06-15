from selenium.webdriver.common.by import By

class StandartItemPurchase:
    button_add_backpack_to_cart = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    button_shopping_cart = (By.XPATH, "//a[@class='shopping_cart_link']")
    button_checkout = (By.XPATH, "//button[@id='checkout']")
    input_first_name = (By.XPATH, "//input[@id='first-name']")
    input_last_name = (By.XPATH, "//input[@id='last-name']")
    input_postal_code = (By.XPATH, "//input[@id='postal-code']")
    button_continue = (By.XPATH, "//input[@id='continue']")
    button_finish = (By.XPATH, "//button[@id='finish']")
    div_order_completed = (By.XPATH, "//div[@id='checkout_complete_container']")