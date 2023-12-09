import json

class Booking_app:
    def __init__(self):
        self.rows = 10
        self.col = 8
        self.total = self.rows * self.col
        self.price = 10
        with open('user_data.json', "a+"):
            try:
                with open('user_data.json', 'r') as file:
                    self.user_data = json.load(file)
            except:
                self.user_data = {}

    def display(self):
        print("Cinema: ")

        for i in range(self.rows + 1):
            for j in range(self.col + 1):
                if i==0:
                    if j==0:
                        print(" ", end=" ")
                    else:
                        print(j, end=" ")
                else:
                    if j==0:
                        print(i, end=" ")
                    else:
                        seat = str(i) + str(j)
                        if seat in self.user_data.keys():
                            print("B", end=" ")
                        else:
                            print("S", end=" ")
            print()

    def is_available(self, row, col):
        seat = row + col
        if seat in self.user_data.keys():
            return False
        else:
            return True
        
    def book_ticket(self, name, gender, age, phone):
        user = {}
        row_num = input("Select row number: ")
        col_num = input("Select seat in selected row number: ")
        seat_num = row_num + col_num
        if self.is_available(row_num, col_num):
            if self.total > 60:
                if int(row_num) > self.rows//2:
                    self.price = 8
                else:
                    self.price = 10
            else:
                self.price = 10
            print("Price of the seat: ", self.price)
            print("Do you wish to continue")
            cont = input(print("Enter Y to continue or N to exit: "))
            if cont == "Y":
                user["Name"] = name
                user["Gender"] = gender
                user["Age"] = age
                user["Phone_number"] = phone
                user["Price"] = self.price
                self.user_data[seat_num] = user

                with open("user_data.json", "w") as file:
                    json.dump(self.user_data, file)
                    print("------Booked Successfully------")

            elif cont == "N":
                print("------Thank You------")

        else:
            print("------Seat not available------")

    def statistics(self):
        purchased_tickets = len(self.user_data.keys())
        percentage = (purchased_tickets / self.total) * 100
        current_income = 0
        for k, v in self.user_data.items():
            current_income += v["Price"]
        if self.total > 60:
            half = self.rows // 2
            total1 = (half * self.col) * 10
            total2 = (self.rows - half) * self.col * 8
            total_income = total1 + total2
        else:
            total_income = self.rows * 10

        stats = f"Number of purchased tickets: {purchased_tickets}\nPercentage of tickets sold: {percentage}\nCurrent Income: {current_income}\nTotal Income: {total_income}"
        print(stats)

    def show_booked_tickets(self):
        for k, v in self.user_data.items():
            print("Seat Number: ", k, end="--->")
            print("User info: ", v)