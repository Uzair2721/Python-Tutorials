# step 1: import tkinter
from tkinter import *
import tkinter.messagebox

# step 2: GUI interaction
window = Tk()

# step 3: adding inputs
# tkinter.messagebox.showinfo("Info", "Running out of time")
# tkinter.messagebox.showwarning("Info", "Running out of time")
# tkinter.messagebox.showerror("Info", "Running out of time")
# question = tkinter.messagebox.askyesno("Whether", "Do you wish to continue")
question = tkinter.messagebox.askokcancel("Whether", "Do you wish to continue")

if question == True:
    print("Continue Installation")
else:
    print("Okay")

# step 4: mainloop
window.mainloop()