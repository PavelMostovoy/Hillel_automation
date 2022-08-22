"""
Make function that receive list and return set
"""
# import pytest

VARIABLE = 123

print("Script file run !")


def converter(list_data: list) -> set:
    """
    Function receive list and return set
    """
    temporary_value = set(list_data)
    if isinstance(list_data, str):
        raise ValueError("Our custom error")
    return temporary_value


#
# if __name__ == "__main__":
#
#     predefined_data = (list(), set(), "string", int(), tuple(), dict(),
#     bool())
#
#
#     def testing():
#         for item in predefined_data:
#             try:
#                 converter(item)
#             except BaseException as er:
#                 print(f"Error found for {item}. error :{er}")
#                 continue
#             print(f"no error for item {item}")
#
#     testing()

def test_function():
    predefined_data = (list(), set(), "string", int(), tuple(), dict(), bool())
    for item in predefined_data:
        try:
            converter(item)
        except BaseException as er:
            print(f"Error found for {item}. error :{er}")
            continue
        print(f"no error for item {item}")


def test_function_1():
    predefined_data = (list(), bool())
    for item in predefined_data:
        try:
            converter(item)
        except BaseException as er:
            raise AssertionError("failed")

            print(f"Error found for {item}. error :{er}")
            continue
        print(f"no error for item {item}")


def test_function_2():
    predefined_data = (list(), set(), "string", int(), tuple(), dict(), bool())
    for item in predefined_data:
        try:
            converter(item)
        except BaseException as er:
            print(f"Error found for {item}. error :{er}")
            continue
        print(f"no error for item {item}")
