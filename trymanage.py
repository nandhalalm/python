users = []
admin_credentials = {'admin': '123'}

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            admin_section()
        elif choice == '2':
            user_section()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

def admin_section():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if admin_credentials.get(username) == password:
        while True:
            print("\n--- Admin Menu ---")
            print("1. View Pending Users")
            print("2. View Accepted Users")
            print("3. delete user")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                manage_pending_users()
            elif choice == '2':
                view_users('Accepted')
            elif choice == '3':
                delete_user()

                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Invalid admin credentials.")

def manage_pending_users():
    print("\n--- Pending Users ---")
    for user in users:
        if user['status'] == 'Pending':
            print(f"ID: {user['userId']}, Name: {user['name']}")
            action = input("Type 'accept' to approve or 'reject' to deny: ")
            if action.lower() == 'accept':
                user['status'] = 'Accepted'
                print(f"{user['name']}'s registration approved.")
            elif action.lower() == 'reject':
                user['status'] = 'Rejected'
                print(f"{user['name']}'s registration rejected.")

def view_users(status):
    print(f"\n--- {status} Users ---")
    for user in users:
        if user['status'] == status:
            print(f"ID: {user['userId']}, Name: {user['name']}")

def delete_user():
    username=input("enter user to delete")
    for user in users:
        if user["username"]== username:
            users.remove(user)
            print("user deleted successfully")
            return
    print("user not found")

def user_section():
    while True:
        print("\n--- User Menu ---")
        print("1. Registration")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

def register_user():
    userId = input("Enter user ID: ")
    name = input("Enter name: ")
    username = input("Enter username: ")
    
    password = input("Enter password: ")
    
    new_user = {
        'userId': userId,
        'name': name,
        'username': username,
        'password': password,
        'balance': 1000,
        'status': 'Pending'
    }
    users.append(new_user)
    print("Registration successful. Your status is pending approval.")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user['username'] == username and user['password'] == password:
            if user['status'] == 'Accepted':
                user_menu(user)
                return
            else:
                print("Your registration is not approved yet.")
                return
    print("Invalid username or password.")

def user_menu(user):
    while True:
        print("\n--- User Menu ---")
        print("1. Deposit Amount")
        print("2. Withdraw Amount")
        print("3. View Profile")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            user['balance'] += amount
            print(f"Deposited {amount}. New balance: {user['balance']}")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= user['balance']:
                user['balance'] -= amount
                print(f"Withdrew {amount}. New balance: {user['balance']}")
            else:
                print("Insufficient funds.")
        elif choice == '3':
            print(f"\n--- User Profile ---\nID: {user['userId']}\nName: {user['name']}\nBalance: {user['balance']}")
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
