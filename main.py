class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

class VendingMachine:
    def __init__(self):
        self.beverages = [
            Beverage("Coke", 1.50),
            Beverage("Pepsi", 1.50),
            Beverage("Water", 1.00),
            Beverage("Juice", 2.00),
            Beverage("Tea", 1.25),
            Beverage("Coffee", 1.75),
        ]

    def display_menu(self):
        print("\nAvailable Beverages:")
        for idx, beverage in enumerate(self.beverages, start=1):
            print(f"{idx}. {beverage}")

    def vend_beverage(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("\nSelect a beverage by entering the number (1-6): "))
                if 1 <= choice <= len(self.beverages):
                    selected_beverage = self.beverages[choice - 1]
                    print(f"\nYou selected: {selected_beverage}")

                    money_inserted = float(input(f"Insert money (${selected_beverage.price:.2f} required): "))
                    if money_inserted >= selected_beverage.price:
                        change = money_inserted - selected_beverage.price
                        print(f"\nVending {selected_beverage.name}... Enjoy!")
                        if change > 0:
                            print(f"Your change: ${change:.2f}")
                    else:
                        print(f"\nInsufficient funds. Please add ${selected_beverage.price - money_inserted:.2f} more.")
                else:
                    print("\nInvalid choice. Please select a number between 1 and 6.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")

if __name__ == "__main__":
    machine = VendingMachine()
    print("Welcome to the Vending Machine!")
    machine.vend_beverage()