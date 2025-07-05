'''
Create a class of student having the following attributes:
- name  
- roll number
-email
total marks

'''

class Student:
    def __init__(self, name, roll_number, email, total_marks):
        self.name = name
        self.roll_number = roll_number
        self.email = email
        self.total_marks = total_marks

    def student_details(self):
        print (f"Name: {self.name}")
        print (f"Roll Number: {self.roll_number}")
        print (f"Email: {self.email}")  
        print (f"Total Marks: {self.total_marks}")

    def check_marks(self,other):
        if self.total_marks >= other.total_marks:
            print(f"{self.name} has passed with {self.total_marks} marks.")
        else:
            print(f"{self.name} has failed with {self.total_marks} marks.")    

s1 = Student("Alice", 101,'alice@gmail.com',712)
s2 = Student("Bob", 102,'bob@gmail.com', 650)

s1.student_details()
s2.student_details()
