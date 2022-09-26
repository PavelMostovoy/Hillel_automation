import threading
import time
from random import randint

value = 0


def myfunc(a, b):
    global value
    value = randint(1, 3)
    time.sleep(value + b)
    print(f"\nThread {a}, seonds to run = {value}")


thr1 = threading.Thread(target=myfunc, args=(1, 2)).start()
thr2 = threading.Thread(target=myfunc, args=(2, 2)).start()
thr3 = threading.Thread(target=myfunc, args=(3, 2)).start()
