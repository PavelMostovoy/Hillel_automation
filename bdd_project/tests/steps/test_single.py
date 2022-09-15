from pytest_bdd import scenarios

file_name = "../features/web_example.feature"
file_name_2 = "../features/name_comparation.feature"

scenarios(file_name, file_name_2)
