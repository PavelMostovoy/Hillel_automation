from behave import *

use_step_matcher("re")


class Users:
    users_list = []

    def get_name(self, item: int):
        return self.users_list[item]

    def set_name(self, name):
        self.users_list.append(name)

    def get_list(self):
        return users.users_list


users = Users()


@given('we have behave installed')
def step_impl(context):
    print("inrernaly added test")
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@given("User '(?P<name>.+)'")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """
    context.first_user = name


@when("Add additional user '(?P<name>.+)'")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name_1: str
    """
    context.execute_steps("Given we have behave installed")
    context.second_user = name


@then("Compare Users names")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    users.set_name(context.first_user)
    # first_user = context.first_user
    second_user = context.second_user
    assert users.get_name(0) == second_user, \
        f"Users name are unexpected {users.get_name(0)}, {second_user}, " \
        f"{users.get_list()} "
