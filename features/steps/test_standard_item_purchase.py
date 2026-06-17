from pytest_bdd import given, when, then, scenario
from pages.actions.Standard_item_purchase_actions import StandardItemPurchaseActions
import pytest

# Es para reutilizar el login
from pages.actions.login_actions import LoginActions

@pytest.fixture
def purchase_actions(driver):
    return StandardItemPurchaseActions(driver)

@pytest.fixture
def login_actions(driver):
    return LoginActions(driver)

@scenario("standard_item_purchase.feature", "Purchase an item with a regular user")
def test_standard_item_purchase():
    pass

@given("the user goes to the website")
def step_open_website(purchase_actions: StandardItemPurchaseActions) -> None:
    purchase_actions.load("https://www.saucedemo.com/")

@when("the user enters valid credentials for an standard user")
def step_login(login_actions: LoginActions) -> None:
    login_actions.type_username("standard_user")
    login_actions.type_password("secret_sauce")
    login_actions.click_submit_button()

@when("the user adds an item to the cart")
def step_add_item_to_cart(purchase_actions: StandardItemPurchaseActions) -> None:
    purchase_actions.click_backpack_add_to_cart_button()
    purchase_actions.click_cart_button()
    purchase_actions.click_checkout_button()

@when("the user completes the checkout process")
def step_complete_checkout(purchase_actions: StandardItemPurchaseActions) -> None:
    purchase_actions.type_first_name("Andrea")
    purchase_actions.type_last_name("Soto")
    purchase_actions.type_postal_code("1305000")
    purchase_actions.click_continue_to_checkout_overview()
    purchase_actions.click_finish_button()

@then("the user is shown a thank you message for its order")
def step_check_message(purchase_actions: StandardItemPurchaseActions) -> None:
    assert purchase_actions.item_was_purchased(), "Error: no se mostró el div de orden completada"