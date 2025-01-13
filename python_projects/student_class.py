# Define the student

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):  
        print(f"student name: {self.name}")
        print(f"sstudent age: {self.age}")  

# Example usage

student1 = student("Arnold", 12)
student1.display_info()        