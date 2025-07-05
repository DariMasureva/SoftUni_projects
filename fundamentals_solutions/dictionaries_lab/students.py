students = []
course_to_filter = ""

while True:
    info = input()
    if ":" in info:
        info = info.split(":")
    else:
        if "_" in info:
            info = info.replace("_", " ")

        course_to_filter = info
        break

    name, id_, course = info
    students.append({"name": name, "ID": id_, "course": course})

for student in students:
    if student["course"] == course_to_filter:
        print(f"{student['name']} - {student['ID']}")
