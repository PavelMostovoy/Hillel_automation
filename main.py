import script

print("Hello world")

predefined_data = (list(), set(), "string", int(), tuple(), dict(), bool())


def testing():
    for item in predefined_data:
        try:
            script.converter(item)
        except BaseException as er:
            print(f"Error found for {item}. error :{er}")
            continue
        print(f"no error for item {item}")


print("only open file")
# testing()

# script.converter()
