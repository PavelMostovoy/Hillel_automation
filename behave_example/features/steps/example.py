from behave import *


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@when("we implement a test <User>")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we implement a test <User>')


@given("I put {thing} in a blender,")
def step_impl(context, thing):
    """
    :type context: behave.runner.Context
    :type thing: str
    """
    raise NotImplementedError(u'STEP: Given I put <thing> in a blender,')


@when("I switch the blender on")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I switch the blender on')


@then("it should transform into {}")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(
            u'STEP: Then it should transform into <other thing>')
