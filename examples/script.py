import main_script

print(f"My name is '{__name__}'")

# if __name__ == "script":
#     print("horrai")

VARIABE = 23

main_script.our_funct(1, 3)

def funct(variable):
    VARIABE = 230
    internal = variable
    result = internal + VARIABE

    def new_func():
        int_2 = VARIABE
        int_3 = internal

    return result
