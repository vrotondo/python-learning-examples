# Setting up the inventory dictionary
inventory = {}

# Adding items to the inventory
def add_product(name, quantity, price):
    if name in inventory:
        print(f"Product '{name}' already exists in inventory.")
    else:
        inventory[name] = {"quantity": quantity, "price": price}
        print(f"Product '{name}' added to inventory.")

# Viewing product information
def view_product(name):
    if name in inventory:
        product_info = inventory[name]
        print(f"Product: {name}")
        print(f"\tQuantity: {product_info['quantity']}")
        print(f"\tPrice: ${product_info['price']:.2f}")  # Format price with 2 decimal places
    else:
        print(f"Product '{name}' not found in inventory.")

# Updating product quantities
def update_quantity(name, new_quantity):
    if name in inventory:
        inventory[name]['quantity'] = new_quantity
        print(f"Updated quantity of '{name}' to {new_quantity}.")
    else:
        print(f"Product '{name}' not found in inventory.")

# Removing a product from the inventory
def remove_product(name):
    if name in inventory:
        inventory.pop(name)
        print(f"Product '{name}' removed from inventory.")
    else:
        print(f"Product '{name}' not found in inventory.")

# Main function for the inventory management system
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add New Product")
        print("2. View Product Information")
        print("3. Update Product Quantity")
        print("4. Remove Product")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter product name: ")
            try:
                quantity = int(input("Enter initial quantity: "))
                price = float(input("Enter product price: "))
                add_product(name, quantity, price)
            except ValueError:
                print("Invalid input. Quantity must be an integer and price must be a number.")
        elif choice == "2":
            name = input("Enter product name to view: ")
            view_product(name)
        elif choice == "3":
            name = input("Enter product name to update: ")
            try:
                new_quantity = int(input("Enter new quantity: "))
                update_quantity(name, new_quantity)
            except ValueError:
                print("Invalid input. Quantity must be an integer.")
        elif choice == "4":
            name = input("Enter product name to remove: ")
            remove_product(name)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

'''
def add_product(name, quantity, price):
    """Adds a new product to the inventory dictionary.

    Args:
        name (str): The product name.
        quantity (int): The initial quantity of the product.
        price (float): The product price.
    """

    if name not in inventory:
        inventory[name] = {"quantity": quantity, "price": price}
    else:
        print(f"Product '{name}' already exists in inventory.")

def view_product(name):
    """Displays information about a product in the inventory.

    Args:
        name (str): The name of the product to view.
    """

    if name in inventory:
        product_info = inventory[name]
        print(f"Product: {name}")
        print(f"\tQuantity: {product_info['quantity']}")
        print(f"\tPrice: ${product_info['price']:.2f}")  # Format price with 2 decimal places
    else:
        print(f"Product '{name}' not found in inventory.")

def update_quantity(name, new_quantity):
    """Updates the quantity of a product in the inventory.

    Args:
        name (str): The name of the product to update.
        new_quantity (int): The new quantity value.
    """

    if name in inventory:
        inventory[name]["quantity"] = new_quantity
        print(f"Product '{name}' quantity updated.")
    else:
        print(f"Product '{name}' not found in inventory.")

def remove_product(name):
    """Removes a product from the inventory.

    Args:
        name (str): The name of the product to remove.
    """

    if name in inventory:
        inventory.pop(name)  # Remove product using pop method
        print(f"Product '{name}' removed from inventory.")
    else:
        print(f"Product '{name}' not found in inventory.")

def main():
    """Main program loop for user interaction."""

    inventory = {}  # Empty dictionary to store inventory data

    while True:
        print("\nInventory Management System")
        print("1. Add New Product")
        print("2. View Product Information")
        print("3. Update Product Quantity")
        print("4. Remove Product")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter product name: ")
            quantity = int(input("Enter initial quantity: "))
            price = float(input("Enter product price: "))
            add_product(name, quantity, price)
        elif choice == "2":
            name = input("Enter product name to view: ")
            view_product(name)
        elif choice == "3":
            name = input("Enter product name to update: ")
            new_quantity = int(input("Enter new quantity: "))
            update_quantity(name, new_quantity)
        elif choice == "4":
            name = input("Enter product name to remove: ")
            remove_product(name)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
'''