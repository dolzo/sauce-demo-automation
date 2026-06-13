from pytest_bdd import given, then, when, scenario
from pages.actions.login_actions import LoginActions

@scenario("login.feature", "Log in into the page with a regular user")
def test_regular_login():
    pass

@given("the user goes to the website")
def step_open_website(driver) -> None:
    login = LoginActions(driver)
    login.load("https://www.saucedemo.com/")

@when("the user enters valid credentials")
def step_login(driver) -> None:
    login = LoginActions(driver)
    login.type_username("standard_user")
    login.type_password("secret_sauce")
    login.click_submit_button()


@then("the user is redirected to the main page with its account")
def step_user_redirected_to_main_page(driver) -> None:
    login = LoginActions(driver)
    login.user_is_logged()
