# Vending Machine Program
# Introduction to Programming – Utility App

# Dictionary storing vending machine items
vending_machine = {
    "A1": {"name": "Coffee", "price": 2.50, "stock": 5, "category": "Hot Drinks"},
    "A2": {"name": "Tea", "price": 2.00, "stock": 5, "category": "Hot Drinks"},
    "B1": {"name": "Chips", "price": 1.50, "stock": 7, "category": "Snacks"},
    "B2": {"name": "Chocolate", "price": 1.75, "stock": 6, "category": "Snacks"}
}

def display_menu():
    print("\n--- VENDING MACHINE MENU ---")
    for code, item in vending_machine.items():
        print(f"{code} | {item['name']} | AED {item['price']} | Stock: {item['stock']}")
    print("----------------------------")

def get_item(code):
    return vending_machine.get(code.upper())

def process_payment(price):
    while True:
        try:
            money = float(input("Insert money (AED): "))
            if money < price:
                print("Insufficient funds. Please insert more money.")
            else:
                return money
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def dispense_item(item, change):
    print(f"\nDispensing {item['name']}...")
    print("Please collect your item.")
    print(f"Change returned: AED {change:.2f}")

def vending_machine_app():
    print("Welcome to the Python Vending Machine!")

    while True:
        display_menu()
        code = input("Enter item code (or 'Q' to quit): ").upper()

        if code == "Q":
            print("Thank you for using the Vending Machine. Goodbye!")
            break

        item = get_item(code)

        if not item:
            print("Invalid item code. Please try again.")
            continue

        if item["stock"] <= 0:
            print("Sorry, this item is out of stock.")
            continue

        print(f"You selected {item['name']} - AED {item['price']}")

        money_inserted = process_payment(item["price"])
        change = money_inserted - item["price"]

        item["stock"] -= 1
        dispense_item(item, change)

        another = input("\nWould you like to buy another item? (Y/N): ").upper()
        if another != "Y":
            print("Thank you for your purchase!")
            break
# Run the application
vending_machine_app()