from data import generate_data

our_data = generate_data(5)

for item in our_data:
    if item == 1:
        print("first")
    elif item == 2:
        print("second")
    elif isinstance(item, int):
        print("next one")
    elif item == "a":
        print('string')
    elif item == "12":
        print("not int")
    elif isinstance(item, list):
        for i in item:
            print(i)
    elif isinstance(item, set):
        print(*item)
    elif item == 15:
        print("s 15")
    elif isinstance(item, str):
        print("next one")
    elif item == "b":
        print('string b')
    elif item == "12":
        print("not int")
    elif isinstance(item, dict):
        for i in item:
            print(i)
    elif isinstance(item, tuple):
        print(*item)
