from functions import Booking_app

print("Welcome to BookMyTicket.com")
str = '''Enter 1. To show seats\nEnter 2. To book a ticket\nEnter 3. To show statistics
Enter 4. To show booked tickets info\nEnter 0. To exit'''

obj = Booking_app()
choice = None

while choice != 0:
    print(str)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.display()

    elif choice == 2:
        name = input("Enter your name: ")
        gender = input("Enter your gender: ")
        age = input("Enter your age: ")
        phone = input("Enter your number: ")
        obj.book_ticket(name, gender, age, phone)

    elif choice == 3:
        obj.statistics()

    elif choice == 4:
        obj.show_booked_tickets()

    elif choice == 0:
        break