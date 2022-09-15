from pathlib import Path

full_path = Path(__file__)

root_path = full_path.parent.parent

file_name = "new_file.txt"
resources_folder = "resources"

file_path = root_path.joinpath(resources_folder, file_name)

print(file_path)

with open(file_path, "w") as f:
    f.write("    text \nNew line\n")

with open(file_path, "r+") as f:
    # data = f.readline()
    # data = f.readline()
    # f.write(f" updated {data}")
    new_data = f.read()

print(new_data)

print(f" path for current working directory {Path.cwd()}")
