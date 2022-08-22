from data import generate_data

our_data = generate_data(5)


# for item in our_data:
#     if item == 1:
#         print("first")
#     elif item == 2:
#         print("second")
#     elif isinstance(item, int):
#         print("next one")
#     elif item == "a":
#         print('string')
#     elif item == "12":
#         print("not int")
#     elif isinstance(item, list):
#         for i in item:
#             print(i)
#     elif isinstance(item, set):
#         print(*item)
#     elif item == 15:
#         print("s 15")
#     elif isinstance(item, str):
#         print("next one")
#     elif item == "b":
#         print('string b')
#     elif item == "12":
#         print("not int")
#     elif isinstance(item, dict):
#         for i in item:
#             print(i)
#     elif isinstance(item, tuple):
#         print(*item)


# for item in our_data:
#     match item:
#         case 1:
#             print("first")
#         case 2:
#             print("second")
#         case "a":
#             print("string")
#         case ("a", "b", "c") :
#             print ("expected tuple")
#         case ("3", "d", "c") :
#             print ("expected tuple")


def som_func():
    print("something")


verifaction = {
        1: "first",
        2: "second",
        3: " next one",
        "a": "string",
        "12": "not inr",
        42: som_func
}

for item in our_data:
    if isinstance(item, (list, set)):
        continue
    if item in verifaction:
        print(verifaction[item])
