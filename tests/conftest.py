import pytest


def collect():
    return 42


@pytest.fixture(autouse=True)
def fix_one():
    print("setup")
    yield
    print("Teardown ")


@pytest.fixture()
def fix_special():
    data = collect()
    print("special setup")


@pytest.fixture(scope="module", autouse=True)
def th():
    yield
    print("shutdown docker infrastructure")
