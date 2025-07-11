path = input()
file_name_start_idx = path.rindex("\\")
file_name, extension = path[file_name_start_idx + 1::].split(".")

print(f"File name: {file_name}\nFile extension: {extension}")
