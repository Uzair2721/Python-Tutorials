# step 1: import tkinter
from tkinter import *

# step 2: GUI interaction
window = Tk()

# step 3: adding inputs
window.title("Webpage")
window.geometry("500x500")
window.config(bg="blue")
inp = Label(window, text="Hello World")
inp.pack()

# step 4: mainloop
window.mainloop()