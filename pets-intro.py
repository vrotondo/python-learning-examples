# Step 1: Determine the Object - A Pet
# Step 2: Build the Class
class Pet:
    # Step 3: Build the __init__ Method
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    # Step 4: Build Methods and Attributes
    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.species}."

    def make_sound(self, sound):
        return f"{self.name} says {sound}!"

# Creating instances
dog = Pet("Buddy", "Dog", 3)
cat = Pet("Whiskers", "Cat", 2)

# Using methods
print(dog.describe())  # Output: Buddy is a 3-year-old Dog.
print(cat.make_sound("Meow"))  # Output: Whiskers says Meow!