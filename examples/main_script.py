# def function(argument):
#     internal_var = argument
#
#     def inner_function(another_argument):
#         return internal_var + another_argument
#
#     return inner_function
#
#
# funct_list = []
#
# for i in range(5):
#     funct_list.append(function(i))
#
# print(funct_list)

print("import init")


def our_funct(var, var_1):
    print("Fuct init")
    local_var = 10
    result = var + var_1 + local_var
    return result


list_of_functions = [lambda x, y=i: x + y for i in range(5)]
list_of_functions_new = [lambda x, y=i: x + y for i in range(5)]

n_fu = our_funct

for function in list_of_functions:
    print(function(10))
    for ne_funct in list_of_functions_new:
        print(ne_funct(35))

n_fu(3, 6)
