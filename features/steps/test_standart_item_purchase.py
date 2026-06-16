from pytest_bdd import given, when, then, scenario
from pages.actions.standart_item_purchase_actions import StandartItemPurchaseActions

# Es para reutilizar el login
from pages.actions.login_actions import LoginActions

@scenario("standart_item_purchase.feature", "Purchase an item with a regular user")
def test_standart_item_purchase():
    pass

@given("the user goes to the website")
def step_open_website(driver) -> None:
    item_purchase = StandartItemPurchaseActions(driver)
    item_purchase.load("https://www.saucedemo.com/")

@when("the user enters valid credentials for an standart user")
def step_login(driver) -> None:
    login = LoginActions(driver)
    login.type_username("standard_user")
    login.type_password("secret_sauce")
    login.click_submit_button()

@when("the user adds an item to the cart")
def step_add_item_to_cart(driver) -> None:
    item_purchase = StandartItemPurchaseActions(driver)
    item_purchase.click_backpack_add_to_cart_button()
    item_purchase.click_cart_button()
    item_purchase.click_checkout_button()

@when("the user completes the checkout process")
def step_complete_checkout(driver) -> None:
    item_purchase = StandartItemPurchaseActions(driver)
    item_purchase.type_first_name("Andrea")
    item_purchase.type_last_name("Soto")
    item_purchase.type_postal_code("1305000")
    item_purchase.click_continue_to_checkout_overview()
    item_purchase.click_finish_button()

@then("the user is shown a thank you message for its order")
def step_check_message(driver) -> None:
    item_purchase = StandartItemPurchaseActions(driver)
    assert item_purchase.item_was_purchased(), "Error: no se mostró el div de orden completada"