# IT5016
"""
Shopping list program
Author: Muskan
"""

def get_shoppinglist():
    """
    Collect user input for items and their prices.
    KISS: This function does one thing—gathering the shopping list.
    DRY: No repeated code for item collection.
    """
    shopping_list = []  # List to store item-price tuples.
    total_price = 0     # Accumulates total price of items.

    while True:
        item = input("Enter the name of the item (or type 'done' to finish): ")
        if item.lower() == 'done':
            break  # Exit condition, simple and clear.
        
        try:
            # Attempt to get a valid price.
            price = float(input(f"Enter the price of '{item}': "))
            shopping_list.append((item, price))  # Store item and price.
            total_price += price  # Update total price.
        except ValueError:
            print("Invalid input. Please enter a numeric value for the price.")
    
    return shopping_list, total_price  # Single responsibility: gathering data.

def display_shoppinglist(shopping_list, total_price):
    """
    Display the shopping list and total price.
    Separation of Concerns: This function only handles output.
    Clean Code: Clear function name indicates purpose.
    """
    if shopping_list:  # Check if there are items to display.
        print("\nShopping list:")
        for item, price in shopping_list:
            print(f"{item}, ${price:.2f}")  # Format price for clarity.
        print(f"\nTotal price: ${total_price:.2f}")  # Clear total display.
    else:
        print("Your shopping list is empty.")

def main():
    """
    Main entry point of the program.
    Open/Closed Principle: The program can be extended (e.g., adding features) without modifying existing code.
    YAGNI: Keeping the functionality straightforward without unnecessary features.
    Avoid Premature Optimization: Focus on clear and functional code first.
    """
    print("Welcome to the shopping list program")
    shopping_list, total_price = get_shoppinglist()  # Gather user input.
    display_shoppinglist(shopping_list, total_price)  # Handle output.

# Call the main function to start the program.
main()
Key Principles Highlighted:
KISS (Keep It Simple, Stupid):

The functions are straightforward and focused on single tasks, avoiding unnecessary complexity.
DRY (Don't Repeat Yourself):

The input collection and output display logic are separated into distinct functions, preventing code duplication.
Open/Closed Principle:

The program can be extended with new features (like sorting items) without changing existing functions.
Composition > Inheritance:

While inheritance isn't used here, the design favors using functions to achieve functionality rather than relying on subclassing.
Single Responsibility:

Each function has a clear purpose: get_shoppinglist() gathers input, while display_shoppinglist() handles output.
Separation of Concerns:

Input gathering and output presentation are managed by separate functions, making the code easier to maintain and test.
YAGNI (You Aren’t Gonna Need It):

The program focuses only on essential functionality, avoiding unnecessary features that complicate the code.
Avoid Premature Optimization:

The code is designed for clarity and correctness first, rather than attempting to optimize performance before it's necessary.
Refactor, Refactor, Refactor:

The code is structured in a way that allows for easy refactoring in the future, promoting maintainability.
Clean Code > Clever Code:




