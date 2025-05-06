# Product data (list of dictionaries)
products = [
    {"name": "Laptop", "price": 1200, "rating": 4.5},
    {"name": "Smartphone", "price": 800, "rating": 4.7},
    {"name": "Headphones", "price": 150, "rating": 4.3}
]

# Sorting function that takes a callback
def sort_products(products, key_function):
    return sorted(products, key=key_function)

# Callback functions for sorting
def sort_by_price(product):
    return product["price"]

def sort_by_rating(product):
    return product["rating"]

# Sorting by price
sorted_by_price = sort_products(products, sort_by_price)
print("Sorted by Price:", sorted_by_price)

# Sorting by rating
sorted_by_rating = sort_products(products, sort_by_rating)
print("Sorted by Rating:", sorted_by_rating)