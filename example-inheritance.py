# Parent class: Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

# Child class: Manager (inherits from Employee)
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Reusing Employee attributes
        self.department = department

    def get_details(self):
        return f"Manager: {self.name}, Department: {self.department}, Salary: ${self.salary}"

# Child class: Engineer (inherits from Employee)
class Engineer(Employee):
    def __init__(self, name, salary, specialty):
        super().__init__(name, salary)
        self.specialty = specialty

    def get_details(self):
        return f"Engineer: {self.name}, Specialty: {self.specialty}, Salary: ${self.salary}"

# Creating employee objects
emp1 = Manager("Alice", 80000, "IT")
emp2 = Engineer("Bob", 70000, "Software Development")

# Displaying employee details
print(emp1.get_details())  # Output: Manager: Alice, Department: IT, Salary: $80000
print(emp2.get_details())  # Output: Engineer: Bob, Specialty: Software Development, Salary: $70000