class OurBasic:
    first_parameter = "0001"
    second_parameter = "0002"
    login = "Login"
    password = "password"


class OurNext(OurBasic):
    first_parameter = "1111"
    parmeter_1 = 1


class NewClass:
    second_var = "class var"
    first_var = 4445

    def __init__(self, first_var):
        print("in progress")
        self.first_var = first_var

    @classmethod
    def functionality(cls):
        # cls.second_var = "Class var"
        print(cls.second_var)


#
# obj2 = NewClass(44444)
obj = NewClass("value")
#
# print(obj.first_var)
#
# obj.functionality(45)
#
# print(obj.first_var)
#
# obj.something_new = print
#
# obj.something_new("printed by class")

obj.second_var = "instance_var"

obj.functionality()
print(obj.second_var)
