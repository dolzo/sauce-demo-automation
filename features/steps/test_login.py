from pytest_bdd import given, then, when, scenario
from pages.actions.login_actions import LoginActions
import pytest

@pytest.fixture
def login_actions(driver):
    return LoginActions(driver)

@scenario("login.feature", "Log in into the page with a regular user")
def test_regular_login():
    pass

@given("the user goes to the website")
def step_open_website(login_actions: LoginActions) -> None:
    login_actions.load("https://www.saucedemo.com/")

@when("the user enters valid credentials")
def step_login(login_actions: LoginActions) -> None:
    login_actions.type_username("standard_user")
    login_actions.type_password("secret_sauce")
    login_actions.click_submit_button()


@then("the user is redirected to the main page with its account")
def step_user_redirected_to_main_page(login_actions: LoginActions) -> None:
    assert login_actions.user_is_logged(), "Error: no se mostró el contenedor de la página principal con el usuario logueado"
