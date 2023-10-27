# step 1: import tkinter
from tkinter import *

# step 2: GUI interaction
window = Tk()

# step 3: adding inputs
window.title("Webpage")
window.geometry("500x500")

button = Button(window, text="Button", width=12)
button.place(x=200, y=200)

# step 4: mainloop
window.mainloop()