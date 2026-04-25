class Printer:
    def __init__(self, brand, model, color, weight):
        self.brand = brand
        self.model = model
        self.color = color
        self.weight = weight

    def show_info(self):
        return f'Brand: {self.brand} | Model: {self.model} | Colour: {self.color} | Weight: {self.weight}kg '


class Laser(Printer):
    def __init__(self, brand, model, color, weight, toner_capacity, front_back):
        super().__init__(brand, model, color, weight)
        self.toner_capacity = toner_capacity
        self.front_back = front_back

    def show_info(self):
        return super().show_info() + f'| Toner cap.: {self.toner_capacity}ml | Front/back: {self.front_back}'


class Matrix(Printer):
    def __init__(self, brand, model, color, weight, needle_num, print_routes: bool):
        super().__init__(brand, model, color, weight)
        self.needle_num = needle_num
        self.print_routes = print_routes

    def show_info(self):
        return super().show_info() + f'| Needle number: {self.needle_num} | Show Routes: {self.print_routes}'


# similar to the shopping cart exercise
class PrinterManager:
    def __init__(self):
        self.printers = []

    def add(self, printer):
        self.printers.append(printer)
        print("Printer added successfully!\n")

    def list_all(self):
        if not self.printers:
            print("\nNo printers registered.\n")
            return

        print("\nRegistered Printers:")
        for i, printer in enumerate(self.printers):
            print(f"{i} - {printer.show_info()}")
        print()

    def remove(self, index):
        try:
            removed = self.printers.pop(index)
            print(f"Removed: {removed.model}\n")
        except (ValueError, IndexError):
            print("Invalid index.\n")


def menu():
    manager = PrinterManager()

    while True:
        print("=== PRINTER MENU ===")
        print("1 - Add Printer")
        print("2 - List Printers")
        print("3 - Remove Printer")
        print("0 - Exit")

        option = input("Choose an option: ")

        if option == "1":
            print("\n1 - Laser Printer")
            print("2 - Matrix Printer")
            choice = input("Choose printer type: ")

            brand = input("Brand: ")
            model = input("Model: ")
            color = input("Color: ")
            weight = float(input("Weight (kg): "))

            if choice == "1":
                toner_capacity = int(input("Toner capacity (ml): "))
                front_back = input("Front/Back printing (True/False): ").lower() == "true"
                printer = Laser(brand, model, color, weight, toner_capacity, front_back)

            elif choice == "2":
                needle_num = int(input("Needle number: "))
                print_routes = input("Print routes (True/False): ").lower() == "true"
                printer = Matrix(brand, model, color, weight, needle_num, print_routes)

            else:
                print("Invalid type.\n")
                continue

            manager.add(printer)

        elif option == "2":
            manager.list_all()

        elif option == "3":
            manager.list_all()
            if manager.printers:
                index = int(input("Enter index to remove: "))
                manager.remove(index)

        elif option == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option.\n")

if __name__ == '__main__':
    menu()