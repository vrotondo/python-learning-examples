class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def update_grade(self, new_grade):
        self.grade = new_grade
    
    def get_info(self):
        return f"Student Name: {self.name}, Grade: {self.grade}"
    
student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

print(student1.get_info())  # Output: Student Name: Alice, Grade: A
print(student2.get_info())  # Output: Student Name: Bob, Grade: B   

student1.update_grade("A+")
print(student1.get_info())  # Output: Student Name: Alice, Grade: A+