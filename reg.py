class StudentRegistration:
    def __init__(self, student_name, registration_number):
        self.student_name = student_name
        self.registration_number = registration_number

    def display_registration(self):
        print(f"Student Name: {self.student_name}")
        print(f"Registration Number: {self.registration_number}")

student1 = StudentRegistration("otwiine elizabeth", "s23b13/087")
student1.display_registration()