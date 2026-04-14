# CLI Coffee App

def show_menu():
    print("\nWelcome to CLI Coffee App!")
    print("-------------------------")
    print("Menu:")
    print("1. Espresso        - $2")
    print("2. Cappuccino      - $3")
    print("3. Latte           - $3")
    print("4. Mocha           - $4")

def get_coffee_choice():
    choice = input("Enter your choice (1-4): ")
    coffee_menu = {"1": ("Espresso", 2),
                   "2": ("Cappuccino", 3),
                   "3": ("Latte", 3),
                   "4": ("Mocha", 4)}
    if choice in coffee_menu:
        return coffee_menu[choice]
    else:
        print("Invalid choice! Try again.")
        return get_coffee_choice()

def get_quantity():
    try:
        qty = int(input("Enter quantity: "))
        if qty > 0:
            return qty
        else:
            print("Quantity must be greater than 0.")
            return get_quantity()
    except ValueError:
        print("Please enter a valid number.")
        return get_quantity()

def get_add_ons():
    add_ons = []
    milk = input("Do you want milk? (yes/no): ").lower()
    if milk == "yes":
        add_ons.append("Milk")
    sugar = input("Do you want sugar? (yes/no): ").lower()
    if sugar == "yes":
        add_ons.append("Sugar")
    flavor = input("Do you want chocolate flavor? (yes/no): ").lower()
    if flavor == "yes":
        add_ons.append("Chocolate Flavor")
    return add_ons

def calculate_total(price, quantity, add_ons):
    add_on_price = 0
    for item in add_ons:
        add_on_price += 0.5  # Each add-on costs $0.5
    total = (price + add_on_price) * quantity
    return total

def main():
    orders = []
    while True:
        show_menu()
        coffee, price = get_coffee_choice()
        qty = get_quantity()
        add_ons = get_add_ons()
        total = calculate_total(price, qty, add_ons)
        
        orders.append({
            "coffee": coffee,
            "quantity": qty,
            "add_ons": add_ons,
            "total": total
        })
        
        print("\nYour Order Summary:")
        print(f"{qty} x {coffee}")
        if add_ons:
            print("Add-ons:", ", ".join(add_ons))
        else:
            print("Add-ons: None")
        print(f"Total: ${total:.2f}")
        
        another = input("\nDo you want to order another coffee? (yes/no): ").lower()
        if another != "yes":
            break

    print("\nThank you for your order! Here is your final summary:")
    grand_total = 0
    for order in orders:
        print(f"{order['quantity']} x {order['coffee']} - Add-ons: {', '.join(order['add_ons']) if order['add_ons'] else 'None'} - Total: ${order['total']:.2f}")
        grand_total += order['total']
    print(f"\nGrand Total: ${grand_total:.2f}")

if __name__ == "__main__":
    main()
