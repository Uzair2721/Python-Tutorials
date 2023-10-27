# step 1: import tkinter
from tkinter import *

# step 2: GUI interaction
window = Tk()

# step 3: adding inputs
window.title("Webpage")
window.geometry("500x500")

def log_entry():
    print("Logged in")

button = Button(window, text="LOGIN", command=log_entry, width=12, bg="sky blue", fg="black", font=("bold", 12), activebackground="black", activeforeground="white")
button.pack()

# step 4: mainloop
window.mainloop()