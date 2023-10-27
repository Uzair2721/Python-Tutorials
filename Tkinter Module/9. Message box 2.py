# step 1: import tkinter
from tkinter import *

# step 2: GUI interaction
window = Tk()

# step 3: adding inputs
window.geometry("500x700")
# message = Message(window, text="Python")
# message.pack()

# var = StringVar()
# message = Message(window, textvariable=var, relief=RAISED, padx=20, pady=20)
# var.set("Welcome")
# message.pack()

var = StringVar()
ent_var = StringVar()

def insert():
    result = ent_var.get()
    var.set(result)

message = Message(window, textvariable=var, relief=RAISED, padx=50, pady=50)
entry = Entry(window, textvariable=ent_var)
button = Button(window, text="OK", command=insert)
message.pack()
entry.pack()
button.pack()

# step 4: mainloop
window.mainloop()