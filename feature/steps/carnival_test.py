from behave import given, then, step, when
from selenium import webdriver
from pages.search_cruise import SearchCruise


@given("I am on carnival Home page")
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='...\\...\\..\\..\\drivers\\chromedriver.exe')
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()
    context.driver.get("https://www.carnival.com")


@given('I want to search for a cruise')
def step_impl(context):
    context.search = SearchCruise(context.driver)


@step('I select "{destination}"')
def step_impl(context, destination):
    context.search.select_destination(destination)


@step("The results are displayed on a grid")
def step_impl(context):
    assert context.search.result_in_grid, "Results grid is no selected"
    after_scenario(context)


@step("I select the duration")
def step_impl(context):
    context.search.select_duration()


@step("I Filter by price")
def step_impl(context):
    context.search.filter_by_price()


@then("The results are shown according to the price rage")
def step_impl(context):
    context.search.price_range()
    after_scenario(context)


@step("ordered by the cheaper")
def step_impl(context):
    context.search.order_by_price()
    after_scenario(context)


def after_scenario(context):
    context.driver.close()
    context.driver.quit()
