# Define an Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name  # Employee's name (attribute)
        self.position = position  # Employee's job title (attribute)

    def introduce(self):
        return f"Hi, I'm {self.name} and I work as a {self.position}."

# Creating instances of Employee
employee1 = Employee("Alice", "Software Engineer")
employee2 = Employee("Bob", "Data Scientist")

# Accessing attributes
print(employee1.name)       # Output: Alice
print(employee2.position)   # Output: Data Scientist

# Calling the introduce method
print(employee1.introduce())  # Output: Hi, I'm Alice and I work as a Software Engineer.
print(employee2.introduce())  # Output: Hi, I'm Bob and I work as a Data Scientist.