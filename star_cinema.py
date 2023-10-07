class Star_Cinema:
    def __init__(self) -> None:
        self.hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        hall = Hall(int(rows), int(cols), hall_no)
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}  # this should be a dictionary. Initially empty
        self.__show_list = []  # this should be a list. Initially Empty
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().__init__()

    def _check_id(self, id):
        for show in self.__show_list:
            if show[0] == id:
                return True
        return False

    def _entry_show(self, id, movie_name, time):
        # creating movie show
        show = (id, movie_name, time)
        self.__show_list.append(show)

        # creating 2D seats list in the cinema hall
        self.__seats[id] = [[0 for x in range(self.__cols)] for y in range(self.__rows)]

    def _book_seats(self, id, seat_location):
        for key, value in self.__seats.items():
            if id == key:
                row = seat_location[0] - 1
                col = seat_location[1] - 1

                if row >= self.__rows:
                    print(f"Invalid row input: {row+1}. Max row size is {self.__rows}.")
                    continue

                if col >= self.__cols:
                    print(
                        f"Invalid column input: {col+1}. Max row size is {self.__cols}."
                    )
                    continue

                if value[row][col] == 0:
                    value[row][col] = 1
                    print(
                        f"You have successfully booked a ticket at ({row+1}, {col+1})"
                    )
                else:
                    print(f"Sorry, ({row+1}, {col+1}) this seat is already booked!")

    def _view_show_list(self):
        for show in self.__show_list:
            print(f"MOVIE NAME: {show[1]} \t SHOW ID: {show[0]} \t TIME: {show[2]}")

    def _view_available_seats(self, id):
        # go inside the seats dictionary
        for key, value in self.__seats.items():
            if int(id) == int(key):
                print(f"Seat plan of hall: {self.__hall_no}")
                for arr in value:
                    print(arr)


# Manual cineplex entry
bcc_cinema = Star_Cinema()

# Manual hall creation
bcc_cinema.entry_hall(6, 6, "A")

# Manual show input
bcc_cinema.hall_list[0]._entry_show(111, "Jawan Majhi", "10/10/2023 11:00 AM")
bcc_cinema.hall_list[0]._entry_show(333, "Hajar Bochor Dhore", "12/10/2023 1:00 AM")

# variable to keep track of replica running
run_code = True

# welcome options
welcome_options = [
    "view all shows today",
    "view available seats",
    "book ticket",
    "exit",
]

while run_code:
    print("\n")

    for idx, option in enumerate(welcome_options):
        print(f"{idx + 1}. {option.upper()}")

    print("\n")

    choice = int(input("ENTER OPTION: "))

    # display all shows todays
    if choice == 1:
        print("---------------------------")
        print("Today's show: ")
        for hall in bcc_cinema.hall_list:
            hall._view_show_list()
        print("---------------------------")

    # display available seats
    elif choice == 2:
        show_id = int(input("ENTER SHOW ID: "))
        valid_id = False

        # Check for invalid show id
        while valid_id == False:
            for hall in bcc_cinema.hall_list:
                valid_id = hall._check_id(show_id)
                if valid_id == True:
                    break
            if valid_id == False:
                print(f"Show id {show_id} is invalid!")
                show_id = int(input("ENTER SHOW ID: "))

        print("---------------------------")
        for hall in bcc_cinema.hall_list:
            hall._view_available_seats(show_id)
        print("---------------------------")

    elif choice == 3:
        show_id = int(input("ENTER SHOW ID: "))
        valid_id = False

        while valid_id == False:
            for hall in bcc_cinema.hall_list:
                valid_id = hall._check_id(show_id)
                if valid_id == True:
                    break
            if valid_id == False:
                print(f"Id {show_id} is invalid.")
                show_id = int(input("ENTER SHOW ID: "))

        ticket_amount = int(input("ENTER NUMBER OF TICKETS TO PURCHASE: "))

        print("---------------------------")
        for i in range(ticket_amount):
            row = int(input("ENTER ROW NUMBER: "))
            col = int(input("ENTER COLUMN NUMBER: "))

            for hall in bcc_cinema.hall_list:
                hall._book_seats(show_id, (row, col))
        print("---------------------------")

    elif choice == 4:
        run_code = False
    else:
        print("Enter a valid option!")
