
import random
from school import School


class Person:
    def __init__(self, name) -> None:
        self.name = name


class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(1, 100)


class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)

        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None
        self.gpa = 0.00

    def calculate_final_grade(self):
        if not self.subject_grade:
            self.grade = "F"
            self.gpa = 0.00
            return self.grade

        total_points = 0

        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade)
            total_points += point

        self.gpa = total_points / len(self.subject_grade)
        self.grade = School.value_to_grade(self.gpa)

        return self.grade

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
