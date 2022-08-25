#
# def function(argument):
#     internal_var = argument
#
#     def inner_function(another_argument):
#         return internal_var + another_argument
#
#
#     return inner_function
#
# funct_list = []
#
# for i in range(5):
#     funct_list.append(function(i))
#
#
# print(funct_list)


list_of_functions = [lambda x: x + i for i in range(5)]

for function in range(5):
    print(list_of_functions[function](10))
