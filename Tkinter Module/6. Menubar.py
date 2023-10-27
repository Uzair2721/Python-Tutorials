# step 1: import tkinter
from tkinter import *

# step 2: GUI interaction
window = Tk()

# step 3: adding inputs
menu = Menu(window)
file = Menu(menu, tearoff=1)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_separator()
file.add_command(label="Exit", command=window.quit)

menu.add_cascade(label="File", menu=file)
window.config(menu=menu)

# step 4: mainloop
window.mainloop()