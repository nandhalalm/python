class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")

            choice = input("Select an operation (1-5): ")

            if choice == '5':
                print("Exiting the calculator.")
                break

            if choice in ['1', '2', '3', '4']:
                try:
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                except ValueError:
                    print("Invalid input! Please enter numeric values.")
                    continue

                if choice == '1':
                    result = self.add(a, b)
                    print(f"Result: {a} + {b} = {result}")
                elif choice == '2':
                    result = self.subtract(a, b)
                    print(f"Result: {a} - {b} = {result}")
                elif choice == '3':
                    result = self.multiply(a, b)
                    print(f"Result: {a} * {b} = {result}")
                elif choice == '4':
                    result = self.divide(a, b)
                    print(f"Result: {a} / {b} = {result}")
            else:
                print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    calc = Calculator()
    calc.menu()
