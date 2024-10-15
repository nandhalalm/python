class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, marks):
        # Check for unique roll number
        if any(student.roll_number == roll_number for student in self.students):
            print("Error: Roll number must be unique. This roll number already exists.")
            return
        student = Student(name, roll_number, marks)
        self.students.append(student)
        print(f"Student {name} added successfully.")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        
        print("List of Students:")
        for student in self.students:
            print(f"Name: {student.name}, Roll Number: {student.roll_number}, Marks: {student.marks}")

    def update_student_marks(self, roll_number, new_marks):
        for student in self.students:
            if student.roll_number == roll_number:
                student.update_marks(new_marks)
                print(f"Marks updated for {student.name}.")
                return
        print("Student not found.")

    def display_average_marks(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                avg = student.average_marks()
                print(f"Average marks for {student.name}: {avg:.2f}")
                return
        print("Student not found.")


def main():
    manager = StudentManager()
    while True:
        print("\nStudent Management System")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Update marks of a student")
        print("4. Calculate and display the average marks of a student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student's name: ")
            roll_number = input("Enter student's roll number: ")
            marks = []
            for i in range(3):
                mark = float(input(f"Enter marks for subject {i + 1}: "))
                marks.append(mark)
            manager.add_student(name, roll_number, marks)

        elif choice == '2':
            manager.view_students()

        elif choice == '3':
            roll_number = input("Enter student's roll number to update marks: ")
            new_marks = []
            for i in range(3):
                mark = float(input(f"Enter new marks for subject {i + 1}: "))
                new_marks.append(mark)
            manager.update_student_marks(roll_number, new_marks)

        elif choice == '4':
            roll_number = input("Enter student's roll number to calculate average marks: ")
            manager.display_average_marks(roll_number)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
