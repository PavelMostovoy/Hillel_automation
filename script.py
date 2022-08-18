"""
Make function that receive list and return set
"""

VARIABLE = 123


def converter(list_data: list) -> set:
    """
    Function receive list and return set
    """
    temporary_value = set(list_data)
    if isinstance(list_data, str):
        raise ValueError("Our custom error")
    return temporary_value
