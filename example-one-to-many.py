class Student:
    all_students = []  # Tracks all student instances

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._teacher = None  # Protected attribute
        Student.all_students.append(self)

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("Teacher must be an instance of Teacher class")
        self._teacher = value


class Teacher:
    def __init__(self, name):
        self.name = name

    def students(self):
        """Retrieve all students who have this teacher assigned."""
        return [student for student in Student.all_students if student.teacher == self]

    def add_student(self, student):
        """Assigns a student to this teacher."""
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class")
        student.teacher = self

# Creating a teacher
teacher1 = Teacher("Mr. Johnson")

# Creating students
student1 = Student("Alice", 15)
student2 = Student("Bob", 14)

# Assigning students to the teacher
teacher1.add_student(student1)
teacher1.add_student(student2)

# Checking the teacher's students
for student in teacher1.students():
    print(student.name)  

# Output:
# Alice
# Bob