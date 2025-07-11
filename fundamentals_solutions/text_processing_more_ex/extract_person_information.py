line_count = int(input())

for _ in range(line_count):
    info = input()
    name = info[info.find("@") + 1 : info.find("|")]
    age = info[info.find("#") + 1 :info.find("*")]
    print(f"{name} is {age} years old.")
