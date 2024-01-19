class Warung:
    def __init__(self):
        self.menu = {
            "Nasi Goreng": 15000,
            "Mie Goreng": 12000,
            "Ayam Goreng": 20000,
            "Es Teh": 5000,
            "Es Jeruk": 6000
        }
        self.orders = []

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: Rp {price}")

    def place_order(self, item, quantity):
        if item in self.menu:
            self.orders.append({"item": item, "quantity": quantity})
            print(f"{quantity} {item}(s) added to your order.")
        else:
            print("Item not found in the menu.")

    def calculate_total(self):
        total = 0
        for order in self.orders:
            item = order["item"]
            quantity = order["quantity"]
            total += self.menu[item] * quantity
        return total

    def display_order_summary(self):
        print("\nOrder Summary:")
        for order in self.orders:
            print(f"{order['quantity']} {order['item']}")
        total = self.calculate_total()
        print(f"Total: Rp {total}")


def main():
    warung = Warung()

    while True:
        print("\nWarung Console:")
        print("1. Display Menu")
        print("2. Place Order")
        print("3. View Order Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            warung.display_menu()
        elif choice == "2":
            item = input("Enter the item you want to order: ")
            quantity = int(input("Enter the quantity: "))
            warung.place_order(item, quantity)
        elif choice == "3":
            warung.display_order_summary()
        elif choice == "4":
            print("Thank you for ordering. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
