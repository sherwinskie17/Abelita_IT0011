# Item class definition
class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price:.2f}"

# CRUD Operations
items = []

# Create item
def create_item():
    try:
        item_id = input("Enter Item ID: ")
        if any(item.item_id == item_id for item in items):
            raise ValueError("Item ID already exists.")
        name = input("Enter Item Name: ")
        description = input("Enter Item Description: ")
        price = float(input("Enter Item Price: "))
        if price < 0:
            raise ValueError("Price must be non-negative.")
        new_item = Item(item_id, name, description, price)
        items.append(new_item)
        print("Item created successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Read items
def read_items():
    if not items:
        print("No items available.")
    for item in items:
        print(item)

# Update item
def update_item(item_id):
    for item in items:
        if item.item_id == item_id:
            try:
                name = input("Enter new Item Name: ")
                description = input("Enter new Item Description: ")
                price = float(input("Enter new Item Price: "))
                if price < 0:
                    raise ValueError("Price must be non-negative.")
                item.name = name
                item.description = description
                item.price = price
                print("Item updated successfully!")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            return
    print("Item not found.")

# Delete item
def delete_item(item_id):
    global items
    items = [item for item in items if item.item_id != item_id]
    print("Item deleted successfully!")

# Main menu
def main_menu():
    while True:
        print("\nItem Management Menu:")
        print("[C] - Create Item")
        print("[R] - Read Items")
        print("[U] - Update Item")
        print("[D] - Delete Item")
        print("[Q] - Quit")

        choice = input("Enter your choice: ").upper()

        if choice == 'C':
            create_item()
        elif choice == 'R':
            read_items()
        elif choice == 'U':
            item_id = input("Enter Item ID to update: ")
            update_item(item_id)
        elif choice == 'D':
            item_id = input("Enter Item ID to delete: ")
            delete_item(item_id)
        elif choice == 'Q':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
main_menu()
