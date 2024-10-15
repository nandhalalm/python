class HotelReservationSystem:
    def __init__(self):
        self.admin_credentials = {'admin': 'admin123'}
        self.receptionist_credentials = {'reception': 'reception123'}
        self.guests = {}
        self.rooms = {}
        self.reservations = {}
        self.guest_id_counter = 1
        self.reservation_id_counter = 1

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Admin")
            print("2. Receptionist")
            print("3. Guest")
            print("4. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.admin_section()
            elif choice == '2':
                self.receptionist_section()
            elif choice == '3':
                self.guest_section()
            elif choice == '4':
                print("Exiting the system.")
                break
            else:
                print("Invalid option. Please try again.")

    def admin_section(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        if self.admin_credentials.get(username) == password:
            while True:
                print("\nAdmin Menu:")
                print("1. Add Room")
                print("2. Update Room Details")
                print("3. Remove Room")
                print("4. View All Reservations")
                print("5. Generate Reports")
                print("6. Exit")
                choice = input("Select an option: ")

                if choice == '1':
                    self.add_room()
                elif choice == '2':
                    self.update_room_details()
                elif choice == '3':
                    self.remove_room()
                elif choice == '4':
                    self.view_all_reservations()
                elif choice == '5':
                    self.generate_reports()
                elif choice == '6':
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid credentials.")

    def add_room(self):
        room_number = input("Enter room number: ")
        room_type = input("Enter room type (single/double/suite): ")
        price_per_night = float(input("Enter price per night: "))
        amenities = input("Enter amenities (comma-separated): ")
        availability = True

        self.rooms[room_number] = {
            'type': room_type,
            'price': price_per_night,
            'amenities': amenities.split(','),
            'available': availability
        }
        print("Room added successfully.")

    def update_room_details(self):
        room_number = input("Enter room number to update: ")
        if room_number in self.rooms:
            price_per_night = float(input("Enter new price per night: "))
            availability = input("Is the room available? (yes/no): ").lower() == 'yes'
            self.rooms[room_number]['price'] = price_per_night
            self.rooms[room_number]['available'] = availability
            print("Room details updated successfully.")
        else:
            print("Room not found.")

    def remove_room(self):
        room_number = input("Enter room number to remove: ")
        if room_number in self.rooms:
            del self.rooms[room_number]
            print("Room removed successfully.")
        else:
            print("Room not found.")

    def view_all_reservations(self):
        if self.reservations:
            print("\nAll Reservations:")
            for reservation in self.reservations.values():
                print(reservation)
        else:
            print("No reservations found.")

    def generate_reports(self):
        total_rooms = len(self.rooms)
        occupied_rooms = sum(1 for room in self.rooms.values() if not room['available'])
        available_rooms = total_rooms - occupied_rooms
        revenue = sum(room['price'] for room in self.rooms.values() if not room['available'])

        print(f"Total Rooms: {total_rooms}")
        print(f"Occupied Rooms: {occupied_rooms}")
        print(f"Available Rooms: {available_rooms}")
        print(f"Revenue Generated: ${revenue:.2f}")

    def receptionist_section(self):
        username = input("Enter receptionist username: ")
        password = input("Enter receptionist password: ")

        if self.receptionist_credentials.get(username) == password:
            while True:
                print("\nReceptionist Menu:")
                print("1. Check-In Guest")
                print("2. Check-Out Guest")
                print("3. Make Reservation")
                print("4. Cancel Reservation")
                print("5. View Available Rooms")
                print("6. View Guest Details")
                print("7. Exit")
                choice = input("Select an option: ")

                if choice == '1':
                    self.check_in_guest()
                elif choice == '2':
                    self.check_out_guest()
                elif choice == '3':
                    self.make_reservation()
                elif choice == '4':
                    self.cancel_reservation()
                elif choice == '5':
                    self.view_available_rooms()
                elif choice == '6':
                    self.view_guest_details()
                elif choice == '7':
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid credentials.")

    def check_in_guest(self):
        guest_id = input("Enter guest ID: ")
        room_number = input("Enter room number: ")
        check_in_date = input("Enter check-in date (YYYY-MM-DD): ")

        if room_number in self.rooms and self.rooms[room_number]['available']:
            self.rooms[room_number]['available'] = False
            self.reservations[self.reservation_id_counter] = {
                'guest_id': guest_id,
                'room_number': room_number,
                'check_in_date': check_in_date,
                'status': 'Checked In'
            }
            print(f"Checked in guest {guest_id} to room {room_number}.")
            self.reservation_id_counter += 1
        else:
            print("Room is not available.")

    def check_out_guest(self):
        guest_id = input("Enter guest ID: ")
        room_number = input("Enter room number: ")

        for reservation_id, details in self.reservations.items():
            if details['guest_id'] == guest_id and details['room_number'] == room_number:
                self.rooms[room_number]['available'] = True
                details['status'] = 'Checked Out'
                print(f"Checked out guest {guest_id} from room {room_number}.")
                return
        print("Reservation not found.")

    def make_reservation(self):
        guest_details = {
            'name': input("Enter guest name: "),
            'contact': input("Enter contact details: "),
            'address': input("Enter address: "),
            'username': input("Enter username: "),
            'password': input("Enter password: ")
        }
        guest_id = self.guest_id_counter
        self.guests[guest_id] = guest_details
        self.guest_id_counter += 1

        room_number = input("Enter room number: ")
        check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
        check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

        if room_number in self.rooms and self.rooms[room_number]['available']:
            self.rooms[room_number]['available'] = False
            self.reservations[self.reservation_id_counter] = {
                'guest_id': guest_id,
                'room_number': room_number,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'status': 'Reserved'
            }
            print(f"Reservation made for guest ID {guest_id} in room {room_number}.")
            self.reservation_id_counter += 1
        else:
            print("Room is not available.")

    def cancel_reservation(self):
        reservation_id = int(input("Enter reservation ID to cancel: "))
        if reservation_id in self.reservations:
            room_number = self.reservations[reservation_id]['room_number']
            self.rooms[room_number]['available'] = True
            del self.reservations[reservation_id]
            print("Reservation cancelled successfully.")
        else:
            print("Reservation not found.")

    def view_available_rooms(self):
        print("\nAvailable Rooms:")
        for room_number, details in self.rooms.items():
            if details['available']:
                amenities = ', '.join(details['amenities'])
                print(f"Room Number: {room_number}, Type: {details['type']}, Price: ${details['price']:.2f}, Amenities: {amenities}")

    def view_guest_details(self):
        guest_id = int(input("Enter guest ID: "))
        if guest_id in self.guests:
            print(self.guests[guest_id])
        else:
            print("Guest not found.")

    def guest_section(self):
        while True:
            print("\nGuest Menu:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.register_guest()
            elif choice == '2':
                self.login_guest()
            elif choice == '3':
                break
            else:
                print("Invalid option. Please try again.")

    def register_guest(self):
        guest_details = {
            'name': input("Enter guest name: "),
            'contact': input("Enter contact details: "),
            'address': input("Enter address: "),
            'username': input("Enter username: "),
            'password': input("Enter password: ")
        }
        guest_id = self.guest_id_counter
        self.guests[guest_id] = guest_details
        self.guest_id_counter += 1
        print(f"Registration successful. Your guest ID is {guest_id}.")

    def login_guest(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for guest_id, details in self.guests.items():
            if details['username'] == username and details['password'] == password:
                self.guest_menu(guest_id)
                return
        print("Invalid credentials.")

    def guest_menu(self, guest_id):
        while True:
            print("\nGuest Menu:")
            print("1. View Available Rooms")
            print("2. Make a Reservation")
            print("3. View Reservation Status")
            print("4. Update Personal Information")
            print("5. Cancel Reservation")
            print("6. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.view_available_rooms()
            elif choice == '2':
                self.make_reservation_guest(guest_id)
            elif choice == '3':
                self.view_reservation_status(guest_id)
            elif choice == '4':
                self.update_personal_info(guest_id)
            elif choice == '5':
                self.cancel_reservation_by_guest(guest_id)
            elif choice == '6':
                break
            else:
                print("Invalid option. Please try again.")

    def make_reservation_guest(self, guest_id):
        room_number = input("Enter room number: ")
        check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
        check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

        if room_number in self.rooms and self.rooms[room_number]['available']:
            self.rooms[room_number]['available'] = False
            self.reservations[self.reservation_id_counter] = {
                'guest_id': guest_id,
                'room_number': room_number,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'status': 'Reserved'
            }
            print(f"Reservation made for guest ID {guest_id} in room {room_number}.")
            self.reservation_id_counter += 1
        else:
            print("Room is not available.")

    def view_reservation_status(self, guest_id):
        print("\nYour Reservations:")
        found = False
        for reservation in self.reservations.values():
            if reservation['guest_id'] == guest_id:
                found = True
                print(f"Reservation ID: {self.reservation_id_counter}, Room Number: {reservation['room_number']}, "
                      f"Check-In: {reservation['check_in_date']}, Check-Out: {reservation['check_out_date']}, "
                      f"Status: {reservation['status']}")
        if not found:
            print("No reservations found.")

    def update_personal_info(self, guest_id):
        print("Update your personal information:")
        if guest_id in self.guests:
            self.guests[guest_id]['contact'] = input("Enter new contact details: ")
            self.guests[guest_id]['address'] = input("Enter new address: ")
            print("Personal information updated successfully.")
        else:
            print("Guest not found.")

    def cancel_reservation_by_guest(self, guest_id):
        reservation_id = int(input("Enter reservation ID to cancel: "))
        if reservation_id in self.reservations:
            reservation = self.reservations[reservation_id]
            if reservation['guest_id'] == guest_id:
                room_number = reservation['room_number']
                self.rooms[room_number]['available'] = True
                del self.reservations[reservation_id]
                print("Reservation cancelled successfully.")
            else:
                print("You do not have permission to cancel this reservation.")
        else:
            print("Reservation not found.")

if __name__ == "__main__":
    system = HotelReservationSystem()
    system.main_menu()
