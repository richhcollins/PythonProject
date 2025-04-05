"""Author: Richard Collins, 860-869-6395, richhcollins@gmail.com
Final Project
You are tasked with creating a simple inventory management system for a market. The system should allow users to add, update, view, and remove items from the inventory. Each item in the inventory will have a name, price, quantity, and category.
Functionality:
Add Item: Create a function     add_item that allows users to add a new item to the inventory. Users should input the name, price, quantity, and category of the item.
Update Item: Implement a function     update_item that allows users to update the details of an existing item in the inventory. Users should be able to update the price, quantity, and category of the item.
View Inventory: Develop a function     view_inventory that displays all items in the inventory along with their details (name, price, quantity, and category).
Remove Item: Create a function     remove_item that allows users to remove an item from the inventory based on its name.
Search by Category: Implement a function     search_by_category that allows users to search for items in the inventory based on their category. The function should display all items belonging to the specified category.
Project Structure:
Define a list     inventory to store the items in the market inventory. Each item should be represented as a dictionary with keys for name, price, quantity, and category.
Implement the functions     add_item,     update_item,     view_inventory,     remove_item, and     search_by_category to manage the inventory.
Create a main loop to interact with the user. The loop should prompt the user to choose from various options such as adding, updating, viewing, removing items, or searching by category.
"""

# Auto Parts Inventory Management System

# Define the inventory as a list of dictionaries
inventory = []

# Function to add a part to the inventory
def add_part():
    part_name = input("Enter part name: ")
    part_number = input("Enter part number: ")
    price = float(input("Enter part price: "))
    quantity = int(input("Enter part quantity: "))
    category = input("Enter part category: ")
    compatibility = input("Enter compatibility details (e.g., Make and Model): ")

    # Create a part dictionary and add it to the inventory
    part = {
        "part_name": part_name,
        "part_number": part_number,
        "price": price,
        "quantity": quantity,
        "category": category,
        "compatibility": compatibility
    }
    inventory.append(part)
    print(f"Part: '{part_name}' added successfully!")

# Function to update an existing part in the inventory
def update_part():
    part_name = input("Enter the name of the part to update: ")

    # Search for the part by name
    for part in inventory:
        if part["part_name"].lower() == part_name.lower():
            print("Part found. Enter new details:")
            part["part_number"] = input("Enter new part number: ")
            part["price"] = float(input("Enter new price: "))
            part["quantity"] = int(input("Enter new quantity: "))
            part["category"] = input("Enter new category: ")
            part["compatibility"] = input("Enter new compatibility details: ")
            print(f"Part: '{part_name}' updated successfully!")
            return

    print(f"Part: '{part_name}' not found in the inventory.")

# Function to view all parts in the inventory
def view_inventory():
    if not inventory:
        print("The inventory is empty.")
        return

    print("\nCurrent Inventory:")
    for part in inventory:
        print(
            f"Name: {part['part_name']}, Part Number: {part['part_number']}, "
            f"Price: ${part['price']:.2f}, Quantity: {part['quantity']}, "
            f"Category: {part['category']}, Compatibility: {part['compatibility']}"
        )

# Function to remove a part from the inventory
def remove_part():
    part_name = input("Enter the name of the part to remove: ")

    # Search for the part by name and remove it
    for part in inventory:
        if part["part_name"].lower() == part_name.lower():
            inventory.remove(part)
            print(f"Part: '{part_name}' removed successfully!")
            return

    print(f"Part: '{part_name}' not found in the inventory.")

# Function to search for parts by category
def search_by_category():
    category = input("Enter the category to search for: ")
    found_parts = [part for part in inventory if part["category"].lower() == category.lower()]

    if not found_parts:
        print(f"No parts found in category '{category}'.")
        return

    print(f"\nParts in category '{category}':")
    for part in found_parts:
        print(
            f"Name: {part['part_name']}, Part Number: {part['part_number']}, "
            f"Price: ${part['price']:.2f}, Quantity: {part['quantity']}, "
            f"Category: {part['category']}, Compatibility: {part['compatibility']}"
        )

# Main menu loop
def main():
    while True:
        print("\n\033[1;34;4mWelcome to the Rich's Auto Parts Warehouse\033[0m")
        print("1. Add Part")
        print("2. Update Part")
        print("3. View Inventory")
        print("4. Remove Part")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_part()
        elif choice == "2":
            update_part()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_part()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("See ya! Come back again!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()