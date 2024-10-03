class Product:
    def __init__(self, product_id, name, description, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price


class User:
    def __init__(self, user_id, name, email, address, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.orders = []


class OnlineShoppingSystem:
    def __init__(self):
        self.admin_credentials = {'admin': 'admin123'}
        self.products = {}
        self.users = {}
        self.orders = []

    def admin_login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        return self.admin_credentials.get(username) == password

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Remove Product")
            print("4. View All Products")
            print("5. View Orders")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.update_product()
            elif choice == '3':
                self.remove_product()
            elif choice == '4':
                self.view_all_products()
            elif choice == '5':
                self.view_orders()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_product(self):
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        self.products[product_id] = Product(product_id, name, description, price)
        print(f"Product '{name}' added successfully!")

    def update_product(self):
        product_id = input("Enter product ID to update: ")
        if product_id in self.products:
            name = input("Enter new product name: ")
            description = input("Enter new product description: ")
            price = float(input("Enter new product price: "))
            self.products[product_id] = Product(product_id, name, description, price)
            print(f"Product '{product_id}' updated successfully!")
        else:
            print("Product not found.")

    def remove_product(self):
        product_id = input("Enter product ID to remove: ")
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product '{product_id}' removed successfully!")
        else:
            print("Product not found.")

    def view_all_products(self):
        print("\nAll Products:")
        for product in self.products.values():
            print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}")

    def view_orders(self):
        print("\nAll Orders:")
        for order in self.orders:
            print(order)

    def register_user(self):
        user_id = input("Enter user ID: ")
        if user_id in self.users:
            print("User ID already exists. Please choose a different ID.")
            return

        email = input("Enter email: ")
        if any(user.email == email for user in self.users.values()):
            print("Email already registered. Please choose a different email.")
            return

        name = input("Enter name: ")
        address = input("Enter address: ")
        password = input("Enter password: ")
        self.users[user_id] = User(user_id, name, email, address, password)
        print(f"User '{name}' registered successfully!")

    def user_login(self):
        user_id = input("Enter user ID: ")
        password = input("Enter password: ")
        user = self.users.get(user_id)
        if user and user.password == password:
            return user
        else:
            print("Invalid credentials.")
            return None

    def user_menu(self, user):
        while True:
            print("\nUser Menu:")
            print("1. View All Products")
            print("2. Place Order")
            print("3. View Order History")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.view_all_products()
            elif choice == '2':
                self.place_order(user)
            elif choice == '3':
                self.view_order_history(user)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def place_order(self, user):
        self.view_all_products()
        product_id = input("Enter the product ID to order: ")
        quantity = int(input("Enter the quantity: "))
        if product_id in self.products:
            product = self.products[product_id]
            order = {
                'user_id': user.user_id,
                'product_id': product_id,
                'quantity': quantity,
                'status': 'Processing'
            }
            self.orders.append(order)
            user.orders.append(order)
            print(f"Order placed for {quantity} of '{product.name}'!")
        else:
            print("Product not found.")

    def view_order_history(self, user):
        print("\nOrder History:")
        for order in user.orders:
            print(order)


def main():
    system = OnlineShoppingSystem()

    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            if system.admin_login():
                system.admin_menu()
            else:
                print("Invalid admin credentials.")
        elif choice == '2':
            print("1. Register")
            print("2. Login")
            sub_choice = input("Choose an option: ")

            if sub_choice == '1':
                system.register_user()
            elif sub_choice == '2':
                user = system.user_login()
                if user:
                    system.user_menu(user)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
