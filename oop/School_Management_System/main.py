
from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom


school = School("ABC", "Dhaka")

# Add classrooms
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_calssroom(eight)
school.add_calssroom(nine)
school.add_calssroom(ten)


# Add students
rhanim = Student("Rahim", nine)
karim = Student("Karim", eight)
rakin = Student("Rakin", ten)
etei = Student("Etei", ten)

# Add student IDs
rhanim.id = "S101"
karim.id = "S102"
rakin.id = "S103"
etei.id = "S104"

school.student_admition(rhanim)
school.student_admition(karim)
school.student_admition(rakin)
school.student_admition(etei)


# Add teachers
abul = Teacher("Abul")
kabrul = Teacher("Kabrul")
rakul = Teacher("Rakul")

school.add_teacher("Bangla", abul)
school.add_teacher("English", kabrul)
school.add_teacher("Math", rakul)


# Add subjects
bangla = Subject("Bangla", abul)
english = Subject("English", kabrul)
math = Subject("Math", rakul)
biology = Subject("Biology", rakul)


# Assign subjects to classrooms
eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(math)

nine.add_subject(bangla)
nine.add_subject(english)
nine.add_subject(math)

ten.add_subject(biology)
ten.add_subject(bangla)
ten.add_subject(math)


# Take semester final exams
eight.take_semester_final()
nine.take_semester_final()
ten.take_semester_final()


# Print school report
print(school)


# Show top students of each classroom
for classroom in [eight, nine, ten]:
    print(f"\nTop students of {classroom.name}:")

    for student in classroom.get_top_students():
        print(
            student.name,
            "| GPA:",
            round(student.gpa, 2),
            "| Grade:",
            student.grade
        )
