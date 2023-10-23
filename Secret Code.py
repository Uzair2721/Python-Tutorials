# first letter of each word will become the last letter
# if the length of string is less than 3, reverse the word
# 3 random characters before and after every word

# Hello World
# elloH orldW
# jhnelloHxse idnorldWncd

# import string
# import random

# msg = input("Enter your message: ")
# ED = input("Enter E to encode msg,\nEnter D to decode msg: ")
# a = msg.split()
# if ED == "E":
#     m = []
#     for i in a:
#         rd1 = ''.join(random.choices(string.ascii_letters, k=3))
#         rd2 = ''.join(random.choices(string.ascii_letters, k=3))
#         if len(i) >= 3:
#             x = i[1:] + i[0]
#         elif len(i) < 3:
#             x = i[::-1]

#         y = rd1 + x + rd2
#         m.append(y)
#     print(" ".join(m))

# elif ED == "D":
#     m = []
#     for i in a:
#         x = i[3:-3]
#         if len(i) >= 9:
#             y = x[-1] + x[0:-1]
#         elif len(i) < 9:
#             y = x[::-1]
#         m.append(y)
#     print(" ".join(m))

# else:
#     print("Invalid Response!!!")


# USING FUNCTIONS -

import string
import random

def encode():
    m = []
    for i in a:
        rd1 = ''.join(random.choices(string.ascii_letters, k=3))
        rd2 = ''.join(random.choices(string.ascii_letters, k=3))
        if len(i) >= 3:
            x = i[1:] + i[0]
        elif len(i) < 3:
            x = i[::-1]
        y = rd1 + x + rd2
        m.append(y)
    print(" ".join(m))
    return m

def decode():
    m = []
    for i in a:
        x = i[3:-3]
        if len(i) >= 9:
            y = x[-1] + x[0:-1]
        elif len(i) < 9:
            y = x[::-1]
        m.append(y)
    print(" ".join(m))
    return m

msg = input("Enter your message: ")
CD = input("Enter E for encode\nEnter D for decode: ")
a = msg.split()

if CD == "E":
    encode()
elif CD == "D":
    decode()