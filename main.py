from hotel_booking_system import Room, Reservation, Hotel
def main():
    hotel = Hotel("Happy Stay Hotel")
    hotel.add_room(Room(101, "Single", 100))
    hotel.add_room(Room(102, "Double", 150))
    hotel.add_room(Room(103, "Suite", 200))

    while True:
        print("\nWelcome to the Hotel Booking System")
        print("1. Show available rooms")
        print("2. Make a reservation")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            available_rooms = hotel.show_available_rooms()
            print("Available Rooms: ", available_rooms)
        elif choice == '2':
            name = input("Enter your name: ")
            room_number = int(input("Enter room number: "))
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            print(hotel.make_reservation(name, room_number, check_in_date, check_out_date))
        elif choice == '3':
            print("Thank you for using the hotel booking system.")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()