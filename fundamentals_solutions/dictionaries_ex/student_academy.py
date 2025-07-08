student_grades = {}
logs = int(input())

for _ in range(logs):
    name, grade = input(), float(input())
    if name in student_grades.keys():
        student_grades[name].append(grade)
    else:
        student_grades[name] = [grade]

student_grades = {student: sum(grades)/len(grades) for student, grades in student_grades.items()
                  if sum(grades)/len(grades) >= 4.5}

for student, avrg_grades in student_grades.items():
    print(f"{student} -> {avrg_grades:.2f}")
