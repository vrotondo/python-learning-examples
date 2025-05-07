'''
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = [] # Stores related Course objects

    def enroll(self, course):
        if isinstance(course, Course) and course not in self.courses:
            self.courses.append(course)
            course.students.append(self) # Establish bidirectional relationship

class Course:
    def __init__(self, title):
        self.title = title
        self.students = [] # Stores related Student objects

# Create students and courses
student1 = Student("Alice")
student2 = Student("Bob")

course1 = Course("Math 101")
course2 = Course("History 201")

# Enroll students in courses
student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course1)

# Checking student-course relationships
print(f"{student1.name} is enrolled in: {[course.title for course in student1.courses]}")
# Output: Alice is enrolled in: ['Math 101', 'History 201']

print(f"{course1.title} has students: {[student.name for student in course1.students]}")
# Output: Math 101 has students: ['Alice', 'Bob']
'''
from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name

    def enroll_in_course(self, course):
        Enrollment(self, course)  # Creates a new relationship instance

    def courses(self):
        return [enrollment.course for enrollment in Enrollment.all if enrollment.student == self]

class Course:
    def __init__(self, title):
        self.title = title

    def students(self):
        return [enrollment.student for enrollment in Enrollment.all if enrollment.course == self]

class Enrollment:
    all = []  # Stores all enrollment relationships

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.enrollment_date = datetime.now()
        Enrollment.all.append(self)

# Create students and courses
student1 = Student("Alice")
student2 = Student("Bob")

course1 = Course("Math 101")
course2 = Course("History 201")

# Enroll students in courses
student1.enroll_in_course(course1)
student1.enroll_in_course(course2)
student2.enroll_in_course(course1)

# Checking enrollments
print(f"{student1.name} is enrolled in: {[course.title for course in student1.courses()]}")
# Output: Alice is enrolled in: ['Math 101', 'History 201']

print(f"{course1.title} has students: {[student.name for student in course1.students()]}")
# Output: Math 101 has students: ['Alice', 'Bob']

# Checking the enrollment date
print(f"{student1.name} enrolled in {course1.title} on {Enrollment.all[0].enrollment_date}")
# Output: Alice enrolled in Math 101 on 2023-05-02 08:39:57