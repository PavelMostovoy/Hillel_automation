def pytest_bdd_before_scenario(request, feature, scenario):
    """Called before scenario is executed"""
    pass


def pytest_bdd_after_scenario(request, feature, scenario):
    """Called after scenario is executed (even if one of steps has failed)"""
    pass


def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    """ - Called before step function is executed and it’s arguments
    evaluated"""
    print("screenshop _befor")


def pytest_bdd_before_step_call(request, feature, scenario, step, step_func,
                                step_func_args):
    """- Called before step function is executed with evaluated arguments"""
    pass
    # print("after step")


def pytest_bdd_after_step(request, feature, scenario, step, step_func,
                          step_func_args):
    """- Called after step function is successfully executed"""
    print("without screenshot")


def pytest_bdd_step_error(request, feature, scenario, step, step_func,
                          step_func_args, exception):
    """ - Called when step function failed to execute"""
    # allure.attach("screenshot")
    print("take  error screenshot")


def pytest_bdd_step_func_lookup_error(request, feature, scenario, step,
                                      exception):
    """ - Called when step lookup failed"""
    pass
