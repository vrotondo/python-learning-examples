import random

print("\n\t1: Rock")    #1 = Rock
print("\t2: Paper")     #2 = Paper
print("\t3: Scissors")  #3 = Scissors

# Choose!
computer = random.randint(1,3)
player = int(input("Please choose 1, 2, or 3: "))
# Note the int() around the input. If the user enters an
# incorrect character, this will cause an error.

if player == computer:
    print("It's a tie!")
