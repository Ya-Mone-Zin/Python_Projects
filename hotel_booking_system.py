class Room:
    def __init__(self, room_number, room_type, rate):
        self.room_number = room_number
        self.room_type = room_type
        self.rate = rate
        self.is_available = True

    def book_room(self):
        self.is_available = False

    def release_room(self):
        self.is_available = True

class Reservation:
    def __init__(self, customer_name, room, check_in_date, check_out_date):
        self.customer_name = customer_name
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def make_reservation(self, customer_name, room_number, check_in_date, check_out_date):
        room = next((room for room in self.rooms if room.room_number == room_number and room.is_available), None)
        if room:
            room.book_room()
            reservation = Reservation(customer_name, room, check_in_date, check_out_date)
            self.reservations.append(reservation)
            return f"Reservation successful for {room_number} from {check_in_date} to {check_out_date}"
        else:
            return "Room is not available."

    def show_available_rooms(self):
        return [room.room_number for room in self.rooms if room.is_available]


