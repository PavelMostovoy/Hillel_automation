from script import converter

# print("Hello world")

predefined_data = (list(), set(), "string", int(), tuple(), dict(), bool())


def testing():
    for item in predefined_data:
        try:
            converter(item)
        except BaseException as er:
            print(f"Error found for {item}. error :{er}")
            continue
        print(f"no error for item {item}")


testing()

converter()