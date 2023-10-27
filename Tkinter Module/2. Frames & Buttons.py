# step 1: import tkinter
from tkinter import *

# step 2: GUI interaction
window = Tk()

# step 3: adding inputs
window.title("Webpage")
window.geometry("500x500")
window.config(bg="orange")

# frame1 = Frame(window, bg="green", width=300, height=300, cursor="dot")
# frame2 = Frame(window, bg="yellow", width=300, height=300, cursor="dotbox")

# frame1.pack(side=TOP)
# frame2.pack(side=BOTTOM)

button1 = Button(window, text="button1", bg="blue")
button2 = Button(window, text="button2", bg="red")
button3 = Button(window, text="button3", fg="purple")

button1.pack()
button2.pack()
button3.pack()

# step 4: mainloop
window.mainloop()