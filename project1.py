# Create a Student Management System using Python and Object-Oriented Programming (OOP).

# The system should allow the user to:

# Add a new student.
# View all students.
# Search for a student using Student ID.
# Update a student's marks.
# Delete a student record.
# Display the student with the highest marks.
# Exit the application.
# Student Details

# Each student should have:

# Student ID
# Student Name
# Age
# Marks

class student:
    def __init__(self,student_id,name,age,marks):
        self.studentid = student_id
        self.name = name
        self.age = age
        self.marks = marks



    def display(self):
        print("\n student Id :",self.studentid)
        print("Name :",self.name)
        print("Age:",self.age)
        print("Marks :",self.marks)

    
class Studentmanagementsystem:
    def __init__(self):
        self.students_list = []
    def add_student(self):
        student_id = int(input('Enter student id:'))
        name = input('Enter student name:')
        age = int(input('Enter student age:'))
        marks = float(input('Enter marks:'))

        new_student = student(student_id ,name , age , marks)
        self.students_list.append(new_student)
        print("Student Added Successfully!")

    def view_student(self):
        if len(self.students_list) == 0:
            print('No student found!')
        else:
            for student in self.students_list:
                student.display()

    def search_student(self):
        student_id = int(input("Enter Student Id to search :"))
        for student in self.students_list:
            if student.student_id == student_id:
                print('Student Found')
                student.display()
                return
            
        print('Student Not Found!')

    def update_marks(self):
        student_id = int(input("enter student id :"))
        for student in self.student_list:
            if student.student_id == student_id:
                new_marks = float(input("enter new marks :"))
                student.marks = new_marks
                print("marks updated successfully")
                return
        print("student not found")

    def delete_student(self):
        student_id = int(input('Enter Student Id:'))

        for student in self.student_list:
            if student.student_id == student_id:
                self.student_list.remove(student)
                print('Student Deleated Successfully!')
                return
        print("student Not Found!")

    def display_topper(self):
        if len(self.student_list) == 0:
            print('No Student Available!')
        else:
            topper = self.student_list[0]

            for student in self.student_list:
                if student.marks> topper.marks:
                    topper = student

            print("\nTopper Details")
            topper.display()

sms = Studentmanagementsystem()

while True:

    print("\n ===== STUDENT MANAGMENT SYSTEM =====")
    print("1.Add Student")
    print("2.View Students")
    print("3. Search Student")
    print("4.Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Exit")

    choice = int(input("Enter Your Choice:"))
     
    if choice == 1:
        sms.add_student()
    
    elif choice == 2:
        sms.view_student()
        
    elif choice == 3 :
        sms.search_student

    elif choice == 4:
        sms.update_marks()

    elif choice == 5:
        sms.delete_student()

    elif choice == 6:
        sms.display_topper()

    elif choice == 7:
        break
    else:
        print("Invalid Choice") 