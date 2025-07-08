courses = {}

while (command:=input()) != "end":
    course, student = command.split(" : ")

    if course in courses:
        courses[course].append(student)
    else:
        courses[course] = [student]

for course, student_list in courses.items():
    print(f"{course}: {len(student_list)}")
    for student in student_list:
        print(f"-- {student}")
