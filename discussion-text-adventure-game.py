def forest_adventure():
    print("\nYou venture deeper into the dark forest.")
    print("Suddenly, you encounter a bear!")
    print("What do you want to do?")
    print("1. Fight the bear")
    print("2. Talk to the bear")

    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        print("You cowardly fight the animal and win. You find a treasure chest containing nothing!")
    elif choice == '2':
        print("You strike up a good talk with a bear and find out you two have a lot in common. You realize that friendship was the treasure all along!")
    else:
        print("Invalid choice. You stand still and do nothing.")

def cave_adventure():
    print("\nYou enter the mysterious cave.")
    print("Inside, you find a treasure chest!")
    print("What do you want to do?")
    print("1. Open the chest")
    print("2. Leave it alone")

    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        print("You open the chest and find a pile of gold coins! You are now rich!")
    elif choice == '2':
        print("You leave the chest alone and exit the cave. Sometimes, it's best to leave things as they are.")
    else:
        print("Invalid choice. You stand still and do nothing.")

def beach_adventure():
    print("\nYou walk along the sunny beach.")
    print("You find a message in a bottle!")
    print("What do you want to do?")
    print("1. Read the message")
    print("2. Throw it back into the ocean")

    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        print("The message says: 'You are destined for greatness!'")
    elif choice == '2':
        print("You throw the bottle back into the ocean. Sometimes, it's best to let things go.")
    else:
        print("Invalid choice. You stand still and do nothing.")

def text_adventure_game():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a dark forest. You see many paths ahead of you, but each heading toward a radically different destination. Where would you like to go?")

    while True:
        print("\nOptions:")
        print("1. Explore the dark forest")
        print("2. Venture into the mysterious cave")
        print("3. Walk along the sunny beach")
        print("4. Quit the game")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            forest_adventure()
        elif choice == '2':
            cave_adventure()
        elif choice == '3':
            beach_adventure()
        elif choice == '4':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the game
text_adventure_game()