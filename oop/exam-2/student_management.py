class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False

        # Add student object to database
        StudentDatabase.add_student(self)

    def get_student_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled:
            raise ValueError("Student is already enrolled.")

        self.__is_enrolled = True
        print("Student enrolled successfully.")

    def drop_student(self):
        if not self.__is_enrolled:
            raise ValueError("Student is not enrolled.")

        self.__is_enrolled = False
        print("Student dropped successfully.")

    def view_student_info(self):
        print(f"ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Enrolled: {self.__is_enrolled}")


def find_student(student_id):
    for student in StudentDatabase.student_list:
        if student.get_student_id() == student_id:
            return student

    return None


def main():
    Student(101, "Rahim Ahmed", "CSE")
    Student(102, "Karim Hasan", "EEE")
    Student(103, "Fatima Begum", "BBA")

    while True:
        print("\n===== Student Management System =====")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if not StudentDatabase.student_list:
                print("No students found.")
            else:
                for student in StudentDatabase.student_list:
                    student.view_student_info()
                    print("-" * 30)

        elif choice == "2":
            try:
                student_id = int(input("Enter student ID: "))
                student = find_student(student_id)

                if student is None:
                    raise ValueError("Invalid student ID.")

                student.enroll_student()

            except ValueError as error:
                print("Error:", error)

        elif choice == "3":
            try:
                student_id = int(input("Enter student ID: "))
                student = find_student(student_id)

                if student is None:
                    raise ValueError("Invalid student ID.")

                student.drop_student()

            except ValueError as error:
                print("Error:", error)

        elif choice == "4":
            print("Exiting Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
