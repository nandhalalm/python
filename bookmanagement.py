class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.admin_credentials = {"admin": "password123"}

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. Display All Books")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.update_book()
            elif choice == '3':
                self.delete_book()
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                break
            else:
                print("Invalid option. Please try again.")

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        quantity = int(input("Enter Quantity: "))
        self.books[book_id] = {"title": title, "author": author, "quantity": quantity}
        print(f"Book '{title}' added successfully.")

    def update_book(self):
        book_id = input("Enter Book ID to update: ")
        if book_id in self.books:
            title = input("Enter new Book Title: ")
            author = input("Enter new Book Author: ")
            quantity = int(input("Enter new Quantity: "))
            self.books[book_id] = {"title": title, "author": author, "quantity": quantity}
            print(f"Book ID '{book_id}' updated successfully.")
        else:
            print("Book ID not found.")

    def delete_book(self):
        book_id = input("Enter Book ID to delete: ")
        if book_id in self.books:
            del self.books[book_id]
            print(f"Book ID '{book_id}' deleted successfully.")
        else:
            print("Book ID not found.")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return
        print("\nAll Books:")
        for book_id, details in self.books.items():
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Quantity: {details['quantity']}")

    def user_menu(self):
        while True:
            print("\nUser Menu:")
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
        username = input("Enter a unique username: ")
        if username in self.users:
            print("Username already exists. Please choose a different one.")
            return

        password = input("Enter your password: ")
        # Ensure password is unique
        if any(user_info["password"] == password for user_info in self.users.values()):
            print("Password already taken. Please choose a different one.")
            return
        
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        address = input("Enter your address: ")
        phone_number = input("Enter your phone number: ")

        self.users[username] = {
            "name": name,
            "age": age,
            "address": address,
            "phone_number": phone_number,
            "password": password
        }
        print(f"User '{name}' registered successfully.")

    def login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.users and self.users[username]["password"] == password:
            self.user_actions()
        else:
            print("Invalid username or password.")

    def user_actions(self):
        while True:
            print("\nUser Actions:")
            print("1. Display All Books")
            print("2. Search Book by Name")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.display_books()
            elif choice == '2':
                self.search_book()
            elif choice == '3':
                break
            else:
                print("Invalid option. Please try again.")

    def search_book(self):
        title = input("Enter the title of the book to search: ")
        found_books = [details for details in self.books.values() if title.lower() in details["title"].lower()]

        if found_books:
            print("\nFound Books:")
            for book in found_books:
                print(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")
        else:
            print("No books found with that title.")

def main():
    library = Library()
    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if username in library.admin_credentials and library.admin_credentials[username] == password:
                library.admin_menu()
            else:
                print("Invalid admin credentials.")
        elif choice == '2':
            library.user_menu()
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
