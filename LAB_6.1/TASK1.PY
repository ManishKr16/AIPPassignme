class Student:
    def __init__(self, name, roll_no, course):
        # Constructor to initialize attributes
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def display_details(self):
        # Method to display student details
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)

# Object creation
student1 = Student("Manish", 101, "BCA")
student1.display_details()
