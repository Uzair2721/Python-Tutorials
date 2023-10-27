# step 1: import tkinter
from tkinter import *

# step 2: GUI interaction
window = Tk()

# step 3: adding inputs
c = Canvas(window, width=500, height=500)
c.pack()

c.create_line(0,0,500,500, width=5, fill="orange", dash=(3,3))
c.create_line(0,500,500,0, width=5, fill="green", dash=(3,3))
c.create_rectangle(150, 125, 450, 375, fill="sky blue", outline="red", width=5)

# step 4: mainloop
window.mainloop()