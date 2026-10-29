

class School():
    def __init__(self,name,address) ->None:
        self.name=name
        self.address=address
        self.teacher={}
        self.classroom={}

    def add_calssroom(self,classroom):
        self.classroom[classroom.name]=classroom

    def add_teacher(self,subject,teacher):
        self.teacher[subject]=teacher

    def student_admition(self,student):
        classroom=student.classroom.name
        self.classroom[classroom].add_student(student)


    @staticmethod
    def calculate_grade(marks):
        if marks < 0 or marks > 100:
            return "Invalid Marks"

        elif marks >= 80 and marks <= 100:
            return "A+"

        elif marks >= 70 and marks < 80:
            return "A"

        elif marks >= 60 and marks < 70:
            return "A-"

        elif marks >= 50 and marks < 60:
            return "B"

        elif marks >= 40 and marks < 50:
            return "C"

        elif marks >= 33 and marks < 40:
            return "D"

        elif marks >= 0 and marks < 33:
            return "F"

    @staticmethod
    def grade_to_value(grade):
        grade_map ={
            "A+": 5.00,
            "A": 4.00,
            "A-": 3.50,
            "B": 3.00,
            "C": 2.00,
            "D": 1.00,
            "F": 0.00,
        }
        return grade_map[grade]

    @staticmethod
    def value_to_grade(value):
        if value < 0 or value > 5:
            return "Invalid Value"
        elif value >= 4.50 and value <= 5.00:
            return "A+"
        elif value >= 3.50 and value < 4.50:
            return "A"
        elif value >= 3.00 and value < 3.50:
            return "A-"
        elif value >= 2.00 and value < 3.00:
            return "B"
        elif value >= 1.00 and value < 2.00:
            return "C"
        elif value >= 0.50 and value < 1.00:
            return "D"
        else:
            return "F"

    def __repr__(self):
        for key in self.classroom.key():
            print("All students")
            result=""
            for key, value in self.classroom.items():

                result +=f"___{key.upper()} classroom Students\n"
                for student in value.students:
                 result +=f"{student.name}\n"

                print(result)
                subject=""
                for key, value in self.classroom.items():
                
                    subject +=f"___{key.upper()} classroom subject\n"
                    for sub in value.students:
                     subject +=f"{sub.name}\n"
                     print(subject)
                     # all techers
                     # all students resulet
                     print("students Resulets")
                    for key , value in self.classroom.items():
                        for student in value.students:
                            for k,i in student.marks.items():
                                print(student.name,k,i,student.subject_grade[k]) 
        
                            print(student.calsulate_final_grade)
                    return ""
