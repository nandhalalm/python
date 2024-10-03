class User:
    def __init__(self, user_id, name, age, address, dob, username, password):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.address = address
        self.dob = dob
        self.username = username
        self.password = password
        self.balance = 1000
        self.status = 'Pending'

class BankManagementSystem:
    def __init__(self):
        self.users = []
        self.admin_credentials = {'admin': 'password123'}
        self.current_user = None

    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Admin")
            print("2. User")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.admin_section()
            elif choice == '2':
                self.user_section()
            elif choice == '3':
                print("Exiting the system.")
                break
            else:
                print("Invalid option. Please try again.")

    def admin_section(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        if self.admin_credentials.get(username) == password:
            while True:
                print("\n--- Admin Menu ---")
                print("1. View Registered Users (Pending)")
                print("2. View Users (Accepted)")
                print("3. View Users (Rejected)")
                print("4. Exit")
                choice = input("Choose an option: ")

                if choice == '1':
                    self.view_pending_users()
                elif choice == '2':
                    self.view_accepted_users()
                elif choice == '3':
                    self.view_rejected_users()
                elif choice == '4':
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid admin credentials.")

    def view_pending_users(self):
        print("\n--- Pending Users ---")
        for user in self.users:
            if user.status == 'Pending':
                print(f"ID: {user.user_id}, Name: {user.name}")
                action = input("Type 'accept' to approve or 'reject' to deny: ")
                if action.lower() == 'accept':
                    user.status = 'Accepted'
                    print(f"{user.name}'s registration approved.")
                elif action.lower() == 'reject':
                    user.status = 'Rejected'
                    print(f"{user.name}'s registration rejected.")
                else:
                    print("Invalid action.")

    def view_accepted_users(self):
        print("\n--- Accepted Users ---")
        for user in self.users:
            if user.status == 'Accepted':
                print(f"ID: {user.user_id}, Name: {user.name}")

    def view_rejected_users(self):
        print("\n--- Rejected Users ---")
        for user in self.users:
            if user.status == 'Rejected':
                print(f"ID: {user.user_id}, Name: {user.name}")

    def user_section(self):
        while True:
            print("\n--- User Menu ---")
            print("1. Registration")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.login_user()
            elif choice == '3':
                break
            else:
                print("Invalid option. Please try again.")

    def register_user(self):
        user_id = input("Enter user ID: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        address = input("Enter address: ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        new_user = User(user_id, name, age, address, dob, username, password)
        self.users.append(new_user)
        print("Registration successful. Your status is pending approval.")

    def login_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in self.users:
            if user.username == username and user.password == password:
                if user.status == 'Accepted':
                    self.current_user = user
                    self.user_menu()
                    return
                else:
                    print("Your registration is not approved yet.")
                    return
        print("Invalid username or password.")

    def user_menu(self):
        while True:
            print("\n--- User Menu ---")
            print("1. Deposit Amount")
            print("2. Withdraw Amount")
            print("3. View Profile")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.deposit_amount()
            elif choice == '2':
                self.withdraw_amount()
            elif choice == '3':
                self.view_profile()
            elif choice == '4':
                self.current_user = None
                break
            else:
                print("Invalid option. Please try again.")

    def deposit_amount(self):
        amount = float(input("Enter amount to deposit: "))
        self.current_user.balance += amount
        print(f"Deposited {amount}. New balance: {self.current_user.balance}")

    def withdraw_amount(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.current_user.balance:
            self.current_user.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.current_user.balance}")
        else:
            print("Insufficient funds.")

    def view_profile(self):
        print("\n--- User Profile ---")
        print(f"ID: {self.current_user.user_id}")
        print(f"Name: {self.current_user.name}")
        print(f"Age: {self.current_user.age}")
        print(f"Address: {self.current_user.address}")
        print(f"DOB: {self.current_user.dob}")
        print(f"Balance: {self.current_user.balance}")

if __name__ == "__main__":
    bank_system = BankManagementSystem()
    bank_system.main_menu()
