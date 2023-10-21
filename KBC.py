print("!!!Welcome To KBC!!!")
print(input("Enter Contestant Name: "))
print("Let's Play")

questions = [
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Munich", "Rome", "Warsaw", "Berlin", "D"],
    ["What is the capital of Germany", "Munich", "Rome", "Berlin", "Warsaw", "C"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
    ["What is the capital of Germany", "Berlin", "Munich", "Rome", "Warsaw", "A"],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion {i+1} for Rs.{levels[i]}")
    print(question[0])
    print(f"A. {question[1]}            B. {question[2]}")
    print(f"C. {question[3]}            D. {question[4]}")
    reply = input("Enter your answer (A-D) or Q to quit: ")
    if reply == "Q":
        if i==0:
            money = 0
        else:
            money = levels[i-1]
        print("Thank You for playing")
        break

    if reply == question[-1]:
        print(f"Correct Answer, you have won Rs.{levels[i]}")
        if i==4:
            money = 10000
        elif i==9:
            money = 320000
        elif i==14:
            money = 10000000
            print("\nCongratulations, you have won 1 crore Rupees!!!")

    else:
        print("\nWrong answer!")
        print("Thank You for playing")
        break

print(f"Your winning: {money}")
    