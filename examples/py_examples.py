import time


def decorated(funct):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = funct(*args, **kwargs)
        print(time.perf_counter() - start)
        return result

    return inner


@decorated
def calc_fun(var: int):
    result = []
    for i in range(var):
        result.append(i * var)
    return result


def calc_fun_01(var: int):
    result = []
    i = 0
    while i < var:
        i += 1
        result.append(i * var)
    return result


def func_1():
    for i in range(100):
        _ = i ** i


def time_counter(var_f, var_value=10):
    start = time.perf_counter()
    var_f(var_value)
    print(time.perf_counter() - start)


decorated_funct = decorated(calc_fun_01)

print(calc_fun(10))

decorated_funct(10)
