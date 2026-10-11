
class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self):
        return f"Student: {self.name}, Class: {self.current_class}, ID: {self.id}"


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f"Teacher: {self.name}, Subject: {self.subject}, ID: {self.id}"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def enroll_student(self, name, current_class):
        student_id = len(self.students) + 1
        student = Student(name, current_class, student_id)
        self.students.append(student)
        print(f"{name} enrolled successfully! Student ID: {student_id}")

    def add_teacher(self, name, subject):
        teacher_id = len(self.teachers) + 101
        teacher = Teacher(name, subject, teacher_id)
        self.teachers.append(teacher)
        print(f"{name} added successfully! Teacher ID: {teacher_id}")

    def show_students(self):
        print(f"\nStudents of {self.name}:")
        for student in self.students:
            print(student)

    def show_teachers(self):
        print(f"\nTeachers of {self.name}:")
        for teacher in self.teachers:
            print(teacher)


# Create school
school = School("Sunrise High School")

# Enroll students
school.enroll_student("Ali Toukir", 9)
school.enroll_student("Karim Hasan", 10)

# Add teachers
school.add_teacher("Rahim Ahmed", "Mathematics")
school.add_teacher("Fatima Begum", "English")

# Display information
school.show_students()
school.show_teachers()
