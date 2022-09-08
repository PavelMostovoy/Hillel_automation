class OurBasic:
    first_parameter = "0001"
    second_parameter = "0002"
    login = "Login"
    password = "password"


class OurNext(OurBasic):
    first_parameter = "1111"
    parmeter_1 = 1


class NewClass:
    __second_var = 456
    first_var = 4445

    def __init__(self, first_var):
        print("in progress")
        self.first_var = first_var
        self.__second_var = f"{first_var} - private"

    @classmethod
    def functionality(cls, x):
        cls.first_var = x * 5
        print(cls.__second_var)


obj2 = NewClass(44444)
obj = NewClass("value")

print(obj.first_var)

obj.functionality(45)

print(obj.first_var)

obj.something_new = print

obj.something_new("printed by class")

print(obj.__second_var)
