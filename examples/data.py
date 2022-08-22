from random import randint

raw_data = (1, 2, 3, 4, 5, "a", "12", [1, 2, 3, "new element"], {1, 4, 5, 6})


def generate_data(addition: int):
    print("starting")
    for item in raw_data:
        yield item
        # print("next one")
        yield randint(0, addition)
        # print("new iteration")


def generate_data_unlim(addition: int):
    print("starting")
    while True:
        yield randint(0, addition)
        # print("next one")
        yield randint(0, addition)
        # print("new iteration")
