class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        seat_list = []
        for i in range(0, self.__rows):
            row = []
            for j in range(0, self.__cols):
                row.append(None)
            seat_list.append(row)
        self.__seats[id] = seat_list

    def book_seats(self, id, seats):
        if id not in self.__seats:
            raise Exception(f"There is no show with id '{id}'")
        for seat in seats:
            if not isinstance(seat, tuple): 
                raise Exception(f"Seat '{seat}' is not a tuple")
            elif seat[0] < 0 or seat[0] >= self.__rows or seat[1] < 0 or seat[1] >= self.__cols:
                raise Exception(f"Invalid seat address: {seat}")
            elif self.__seats[id][seat[0]][seat[1]] is True:
                raise Exception(f"Seat '{seat}' is already booked")
            self.__seats[id][seat[0]][seat[1]] = True
        
    def view_show_list(self):
        return self.__show_list
    
    def view_available_seats(self, id):
        if id not in self.__seats:
            raise Exception(f"There is no show with id '{id}'")
        
        available_seats = []
        for i, row in enumerate(self.__seats[id]):
            for j, col in enumerate(row):
                if col is None:
                    available_seats.append((i,j))
        
        return available_seats

first_hall = Hall(4, 5, 1)

first_hall.entry_show("001", "Dirilis Ertugrul", "04:00PM JAN 09, 2024")
first_hall.entry_show("002", "Payitaht Abdul Hamid", "05:00PM JAN 09, 2024")
first_hall.entry_show("003", "Kingdom of Heaven", "06:00PM JAN 09, 2024")
first_hall.entry_show("004", "The Godfather (Trio)", "07:00PM JAN 09, 2024")

while True:
    print("----------------------------------------")
    print("|  ID: Description                     |")
    print("|  --: -----------------------         |")
    print("|   1: View all running shows          |")
    print("|   2: View available seats in a show  |")
    print("|   3: Book a ticket in a show         |")
    print("|   4: Exit                            |")
    print("----------------------------------------")

    option = input("Enter the option ID: ")

    print()

    try:
        if option == '1':
            shows = first_hall.view_show_list()
            print("Shows List:")
            for show in shows:
                print(f"ID: {show[0]}    Play Time: {show[2]}    Show Name: {show[1]}")

        elif option == '2':
            id = input("Enter the show ID: ")
            seats = first_hall.view_available_seats(id)
            print(f"Available Seats for the show (ID: {id}):")
            for seat in seats:
                print(f"(Row {seat[0]}, Col {seat[1]})")

        elif option == '3':
            id = input("Enter the show ID: ")
            seat_input = input("Enter the row and col no. of the seat (example: 2 3): ").split()
            seat = (int(seat_input[0]), int(seat_input[1]))
            first_hall.book_seats(id, [seat])
            print(f"Success: You booked the seat {seat} for the show (ID: {id})")
        elif option == '4':
            break
        else:
            raise Exception(f"{option} is an invalid option")
    except Exception as e:
        print(f"Failed: {e}")
    
    print()
