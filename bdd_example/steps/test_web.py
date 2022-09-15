from pytest_bdd import scenario, given, when, then, scenarios, parsers
import requests
from assertpy import assert_that

scenarios('web_test.feature')

data = {"Test1": {"user_name": "admin", "password": "admin123"},
        "Test2": {"user_name": "ad", "password": "ad"}}


@given(parsers.re("I'm an user '(?P<user>.*)'"))
def step_impl(request, user):
    user_name = data[user]
    print(user_name)
    request.user = user_name


@given(parsers.re("I have endpoint'(?P<endpoint>.*)'"))
def step_impl(request, endpoint):
    request.endpoint = endpoint


@when("I go to endpoint page")
def step_impl(request):
    authentication = request.user["user_name"], request.user["password"]
    request.response = requests.get(request.endpoint, auth=authentication)


@then(parsers.re("I should receive '(?P<code>.*)' code"))
def step_impl(request, code):
    code = int(code)
    status_code = request.response.status_code
    assert_that(status_code, f" Received status code {status_code}") \
        .is_equal_to(code)
