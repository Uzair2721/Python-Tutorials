import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
hour = int(time.strftime("%H"))

if 4<=hour<12:
    print("Good Morning")
elif 12<=hour<17:
    print("Good Afternoon")
elif 17<=hour<21:
    print("Good Evening")
else:
    print("Good Night")