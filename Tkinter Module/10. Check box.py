# step 1: import tkinter
from tkinter import *

# step 2: GUI interaction
window = Tk()

# step 3: adding inputs
window.geometry("500x700")

check_box_1 = IntVar()
check_box_2 = IntVar()
check_box_3 = IntVar()

chk_btn_1 = Checkbutton(window, text="Apple", onvalue=1, offvalue=0, height=2, width=10)
chk_btn_2 = Checkbutton(window, text="Orange", onvalue=1, offvalue=0, height=2, width=10)
chk_btn_3 = Checkbutton(window, text="Grapes", onvalue=1, offvalue=0, height=2, width=10)

chk_btn_1.pack()
chk_btn_2.pack()
chk_btn_3.pack()


# step 4: mainloop
window.mainloop()