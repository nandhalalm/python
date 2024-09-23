
users = []

while True:
    print("Menu:")
    print("1. Add user")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        address = input("Enter address: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        users.append({"name": name, "age": age, "address": address, "username": username, "password": password})
        print("User added successfully")

    elif choice == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Login successful")
                break
        else:
            print("Invalid password")

    elif choice == 3:
        print("Exiting")
        break

    else:
        print("Invalid choice. ")