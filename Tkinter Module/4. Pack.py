# step 1: import tkinter
from tkinter import *

# step 2: GUI interaction
window = Tk()

# step 3: adding inputs
window.title("Webpage")
window.geometry("500x700")

label1 = Label(window, text="Label-1", bg="blue", fg="white")
label2 = Label(window, text="Label-2", bg="green", fg="white")
label3 = Label(window, text="Label-3", bg="orange", fg="white")

label1.pack(side=TOP, fill=X, expand=False)
label2.pack(side=RIGHT, fill=Y, expand=False)
label3.pack(side=LEFT, fill=Y, expand=False)

# step 4: mainloop
window.mainloop()