import random
import time


def first():
    """
    requestor for external system (random)
    :return:
    """
    while True:
        time.sleep(1)
        var = random.randint(1, 10)
        if var == 5:
            yield var * 20
        else:
            yield 0


func = first()
iteration = 0

while True:

    variable = next(func)
    if variable == 0:
        print("Still not correct value\n continue do something")
        print(iteration)
    else:
        print(f"Correct value is {variable}")
        break
    iteration += 1

print("end of program")
