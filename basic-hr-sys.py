class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def give_raise(self, amount):
        self.salary += amount
        return f"{self.name}'s new salary is {self.salary}."
    
    def get_info(self):
        return f"Employee: {self.name}, Position: {self.position}, Salary: {self.salary}"
    
# Creating instances of Employee
employee1 = Employee("Alice", "Software Engineer", 70000)
employee2 = Employee("Bob", "Data Scientist", 80000)

# Accessing instance properties
print(employee1.get_info())  # Output: Employee: Alice, Position: Software Engineer, Salary: 70000

# Using instance methods
print(employee2.give_raise(5000))  # Output: Bob's new salary is 85000.
# Output: Employee: Bob, Position: Data Scientist, Salary: 85000