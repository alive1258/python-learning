from school import School


class Subject:
    def __init__(
        self,
        name,
        teacher,
        max_marks=100,
        pass_marks=33
    ) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = max_marks
        self.pass_marks = pass_marks

    def exam(self, students):
        for student in students:
            marks = self.teacher.evaluate_exam()
            student.marks[self.name] = marks
            student.subject_grade[self.name]=School.calculate_grade(marks)