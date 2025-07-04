class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, student:str, grade:float):
        if len(self.students) < Class.__students_count:
            self.students.append(student)
            self.grades.append(grade)

    def get_average_grade(self):
        average = 0
        if self.grades:
            average = sum(self.grades) / len(self.students)
        return float(f"{average:.2f}")

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"

