import pytest


def setup():
    print("basic setup into module")


def teardown():
    print("basic teardown into module")


# def setup_module(module):
#     print("module setup")
#
#
# def teardown_module(module):
#     print("module teardown")
#

def setup_function(function):
    print("function setup")


def test_numbers_3_4(request):
    print("test 3*4")
    request.data = 345
    assert 3 * 4 == 12


def test_strings_a_3(request):
    local_data = request.data
    print("test a*3")
    assert 'a' * 3 == 'aaa'
