class HotelReservationSystem:
    def __init__(self):
        self.admin_credentials = {"admin": "admin123"}
        self.receptionist_credentials = {"reception": "reception123"}
        self.rooms = {}
        self.reservations = {}
        self.guests = {}
        self.room_id_counter = 1
        self.reservation_id_counter = 1
        self.guest_id_counter = 1

    def main_menu(self):
        while True:
            print("\nMain Menu")
            print("1. Admin")
            print("2. Receptionist")
            print("3. Guest")
            print("4. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                self.admin_section()
            elif choice == "2":
                self.receptionist_section()
            elif choice == "3":
                self.guest_section()
            elif choice == "4":
                print("Exiting the system.")
                break
            else:
                print("Invalid option. Please try again.")

    # Admin Section
    def admin_section(self):
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")
        if self.admin_credentials.get(username) == password:
            while True:
                print("\nAdmin Menu")
                print("1. Add Room")
                print("2. Update Room Details")
                print("3. Remove Room")
                print("4. View All Reservations")
                print("5. Generate Reports")
                print("6. Exit")
                choice = input("Select an option: ")
                if choice == "1":
                    self.add_room()
                elif choice == "2":
                    self.update_room()
                elif choice == "3":
                    self.remove_room()
                elif choice == "4":
                    self.view_all_reservations()
                elif choice == "5":
                    self.generate_reports()
                elif choice == "6":
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid credentials.")

    def add_room(self):
        room_number = input("Enter Room Number: ")
        room_type = input("Enter Room Type (single/double/suite): ")
        price = float(input("Enter Price per Night: "))
        self.rooms[room_number] = {
            "type": room_type,
            "price": price,
            "availability": "available"
        }
        print("Room added successfully.")

    def update_room(self):
        room_number = input("Enter Room Number to Update: ")
        if room_number in self.rooms:
            price = float(input("Enter New Price per Night: "))
            availability = input("Enter Availability Status (available/occupied): ")
            self.rooms[room_number]["price"] = price
            self.rooms[room_number]["availability"] = availability
            print("Room updated successfully.")
        else:
            print("Room not found.")

    def remove_room(self):
        room_number = input("Enter Room Number to Remove: ")
        if room_number in self.rooms:
            del self.rooms[room_number]
            print("Room removed successfully.")
        else:
            print("Room not found.")

    def view_all_reservations(self):
        if not self.reservations:
            print("No reservations found.")
            return
        print("\nAll Reservations:")
        for res_id, details in self.reservations.items():
            print(f"Reservation ID: {res_id}, Guest ID: {details['guest_id']}, Room Number: {details['room_number']}, Status: {details['status']}")

    def generate_reports(self):
        total_rooms = len(self.rooms)
        available_rooms = sum(1 for room in self.rooms.values() if room['availability'] == 'available')
        occupancy_rate = (total_rooms - available_rooms) / total_rooms * 100 if total_rooms > 0 else 0
        print(f"\nTotal Rooms: {total_rooms}, Available Rooms: {available_rooms}, Occupancy Rate: {occupancy_rate:.2f}%")

    # Receptionist Section
    def receptionist_section(self):
        username = input("Enter Receptionist Username: ")
        password = input("Enter Receptionist Password: ")
        if self.receptionist_credentials.get(username) == password:
            while True:
                print("\nReceptionist Menu")
                print("1. Check-In Guest")
                print("2. Check-Out Guest")
                print("3. Make Reservation")
                print("4. Cancel Reservation")
                print("5. View Available Rooms")
                print("6. View and Manage Guest Details")
                print("7. Exit")
                choice = input("Select an option: ")
                if choice == "1":
                    self.check_in_guest()
                elif choice == "2":
                    self.check_out_guest()
                elif choice == "3":
                    self.make_reservation()
                elif choice == "4":
                    self.cancel_reservation()
                elif choice == "5":
                    self.view_available_rooms()
                elif choice == "6":
                    self.view_and_manage_guest_details()
                elif choice == "7":
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid credentials.")

    def check_in_guest(self):
        guest_id = input("Enter Guest ID: ")
        room_number = input("Enter Room Number: ")
        check_in_date = input("Enter Check-In Date (YYYY-MM-DD): ")
        if room_number in self.rooms and self.rooms[room_number]["availability"] == "available":
            self.rooms[room_number]["availability"] = "occupied"
            self.reservations[self.reservation_id_counter] = {
                "guest_id": guest_id,
                "room_number": room_number,
                "check_in_date": check_in_date,
                "status": "checked-in"
            }
            print("Check-in successful. Reservation ID:", self.reservation_id_counter)
            self.reservation_id_counter += 1
        else:
            print("Room is not available.")

    def check_out_guest(self):
        guest_id = input("Enter Guest ID: ")
        room_number = input("Enter Room Number: ")
        for res_id, details in self.reservations.items():
            if details["guest_id"] == guest_id and details["room_number"] == room_number and details["status"] == "checked-in":
                self.rooms[room_number]["availability"] = "available"
                details["status"] = "checked-out"
                print("Check-out successful.")
                return
        print("No active reservation found for this guest.")

    def make_reservation(self):
        guest_name = input("Enter Guest Name: ")
        contact = input("Enter Guest Contact: ")
        address = input("Enter Guest Address: ")
        room_number = input("Enter Room Number: ")
        check_in_date = input("Enter Check-In Date (YYYY-MM-DD): ")
        check_out_date = input("Enter Check-Out Date (YYYY-MM-DD): ")

        if room_number in self.rooms and self.rooms[room_number]["availability"] == "available":
            self.rooms[room_number]["availability"] = "reserved"
            guest_id = self.guest_id_counter
            self.guests[guest_id] = {
                "name": guest_name,
                "contact": contact,
                "address": address
            }
            self.reservations[self.reservation_id_counter] = {
                "guest_id": guest_id,
                "room_number": room_number,
                "check_in_date": check_in_date,
                "check_out_date": check_out_date,
                "status": "reserved"
            }
            print("Reservation successful. Reservation ID:", self.reservation_id_counter, "Guest ID:", guest_id)
            self.reservation_id_counter += 1
            self.guest_id_counter += 1
        else:
            print("Room is not available.")

    def cancel_reservation(self):
        reservation_id = int(input("Enter Reservation ID to cancel: "))
        if reservation_id in self.reservations:
            room_number = self.reservations[reservation_id]["room_number"]
            self.rooms[room_number]["availability"] = "available"
            del self.reservations[reservation_id]
            print("Reservation cancelled successfully.")
        else:
            print("Invalid Reservation ID.")

    def view_available_rooms(self):
        available_rooms = {num: details for num, details in self.rooms.items() if details["availability"] == "available"}
        if available_rooms:
            print("\nAvailable Rooms:")
            for room_number, details in available_rooms.items():
                print(f"Room Number: {room_number}, Type: {details['type']}, Price: ${details['price']}")
        else:
            print("No available rooms.")

    def view_and_manage_guest_details(self):
        print("\nGuest Details:")
        for guest_id, details in self.guests.items():
            print(f"Guest ID: {guest_id}, Name: {details['name']}, Contact: {details['contact']}, Address: {details['address']}")

        guest_id_to_update = int(input("Enter Guest ID to update details (or 0 to skip): "))
        if guest_id_to_update in self.guests:
            new_contact = input("Enter new Contact Details: ")
            new_address = input("Enter new Address: ")
            self.guests[guest_id_to_update]["contact"] = new_contact
            self.guests[guest_id_to_update]["address"] = new_address
            print(f"Guest ID {guest_id_to_update} details updated successfully.")
        elif guest_id_to_update != 0:
            print("Invalid Guest ID.")

    def guest_section(self):
        while True:
            print("\nGuest Menu")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                self.register_guest()
            elif choice == "2":
                self.login_guest()
            elif choice == "3":
                break
            else:
                print("Invalid option. Please try again.")

    def register_guest(self):
        name = input("Enter your Name: ")
        contact = input("Enter your Contact: ")
        address = input("Enter your Address: ")
        username = input("Choose a Username: ")
        password = input("Choose a Password: ")
        guest_id = self.guest_id_counter

        self.guests[guest_id] = {
            "name": name,
            "contact": contact,
            "address": address,
            "username": username,
            "password": password
        }
        print(f"Registration successful. Your Guest ID is {guest_id}.")
        self.guest_id_counter += 1

    def login_guest(self):
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")
        for guest_id, details in self.guests.items():
            if details["username"] == username and details["password"] == password:
                self.guest_menu(guest_id)
                return
        print("Invalid credentials.")

    def guest_menu(self, guest_id):
        while True:
            print("\nGuest Menu")
            print("1. View Available Rooms")
            print("2. Make a Reservation")
            print("3. View Reservation Status")
            print("4. Update Personal Information")
            print("5. Cancel Reservation")
            print("6. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                self.view_available_rooms()
            elif choice == "2":
                self.make_reservation()
            elif choice == "3":
                self.view_reservation_status(guest_id)
            elif choice == "4":
                self.update_personal_information(guest_id)
            elif choice == "5":
                self.cancel_reservation()
            elif choice == "6":
                break
            else:
                print("Invalid option. Please try again.")

    def view_reservation_status(self, guest_id):
        print("\nCurrent Reservations:")
        for res_id, details in self.reservations.items():
            if details["guest_id"] == guest_id:
                print(f"Reservation ID: {res_id}, Room Number: {details['room_number']}, Status: {details['status']}")

    def update_personal_information(self, guest_id):
        print("Updating Personal Information:")
        new_contact = input("Enter new Contact Details: ")
        new_address = input("Enter new Address: ")
        self.guests[guest_id]["contact"] = new_contact
        self.guests[guest_id]["address"] = new_address
        print("Personal information updated successfully.")

if __name__ == "__main__":
    system = HotelReservationSystem()
    system.main_menu()
