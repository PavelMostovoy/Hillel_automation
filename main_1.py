from script import converter

# print("Hello world")

predefined_data = (list(), set(), "string", int(), tuple(), dict(), bool())

errors = []

def testing():
    for item in predefined_data:
        try:
            converter(item)
        except BaseException as er:
            errors.append(f"Item {item} failed with {er}")
            continue



testing()

# assert len(errors) == 0, f"Errors apears {errors}"

print("running")

a, b = 4, 6
assert a > b, "False"


