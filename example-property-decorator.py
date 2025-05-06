APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        '''Getter method - retrieves name'''
        return self._name
    
    @name.setter
    def name(self, name):
        '''Setter method - ensures name is not empty'''
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 25 characters!")
    
    @property
    def breed(self):
        '''Getter method - retrieves breed'''
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        ''''Setter method - ensures breed is in the approved list'''
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError(f"Breed must be one of the following: {', '.join(APPROVED_BREEDS)}")
        
# Registering a valid dog
dog1 = Dog("Buddy", "Corgi")
print(dog1.name)  # Output: Buddy
print(dog1.breed)  # Output: Corgi

# Attempting to set an invalid name
try:
    dog1.name = ""  # Invalid: Name too short
except ValueError as e:
    print(e)  # Output: Name must be a string between 1 and 25 characters.

# Attempting to set an invalid breed
try:
    dog1.breed = "Poodle"  # Invalid: Not in APPROVED_BREEDS
except ValueError as e:
    print(e)  # Output: Breed must be in the list of approved breeds.

# Registering another valid dog
dog2 = Dog("Max", "Beagle")
print(dog2.name)  # Output: Max
print(dog2.breed)  # Output: Beagle