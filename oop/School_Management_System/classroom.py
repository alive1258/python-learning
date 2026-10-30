
class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)

    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)

        for student in self.students:
            student.calculate_final_grade()

    def get_top_students(self):
        return sorted(
            self.students,
            key=lambda student: student.gpa,
            reverse=True
        )
