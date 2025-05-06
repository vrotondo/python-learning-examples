class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Notice the underscore (_) to indicate a "private" attribute

    @property
    def salary(self):
        """Getter method - retrieves salary"""
        return self._salary

    @salary.setter
    def salary(self, value):
        """Setter method - ensures salary is not negative"""
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value

emp = Employee("Alice", 50000)
print(emp.salary)  # Output: 50000
emp.salary = -1000  # Raises ValueError: Salary cannot be negative!