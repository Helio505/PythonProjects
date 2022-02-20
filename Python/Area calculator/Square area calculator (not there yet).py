from PIL import Image, ImageTk
import tkinter
from decimal import Decimal
from tkinter.filedialog import askopenfilename
import sys

# window 1 ----------------------
root_start = tkinter.Tk()
root_start.title("Area")
root_start.geometry("250x400")
root_start.resizable(width=0, height=0)

# This is for the default exit button:
def exit_all():
    sys.exit() # now if the user closes the window, it is intended that they want to close everything, so the whole program stops.

root_start.protocol("WM_DELETE_WINDOW", exit_all)

# this function exits window 1
def exit_window():
    root_start.destroy()

button_start = tkinter.Button(root_start, bg="#ededed", borderwidth=3, relief="raised", padx=40, pady=7, font=("Arial", 14), text="Start app", command=exit_window)
button_start.place(x=35, y=170)

# this func opens the +information window
def open_info_window():
    # This is the information window:
    root_info = tkinter.Tk()
    root_info.title("Info")
    root_start.geometry("250x400")
    root_start.resizable(width=0, height=0)

    label_text_info = tkinter.Label(root_info, text="Please look through this \n information box first        \n before clicking start.        ")
    label_text_info.place(x=20, y=20) 
    root_info.mainloop()

button_info0 = tkinter.Button(root_start, bg="#ededed", borderwidth=3, relief="raised", padx=5, pady=2, font=("Arial", 14), text="i", command=open_info_window)
button_info0.place(x=35, y=100)

root_start.mainloop()




# window 2 ----------------------
root = tkinter.Tk()
root.title("Area")
root.geometry("250x400")
root.resizable(width=0, height=0)

label = tkinter.Label(root, width=22, borderwidth=5, relief="groove", font=("Arial", 12), bg="white", text="The results will appear here")
label.place(x=20, y=20)

# block of code responsible for instantiating the image:
imageOpened = Image.open("square.png")
global tkimage
tkimage_square = ImageTk.PhotoImage(imageOpened)
square = tkinter.Label(root, image=tkimage_square)
square.place(x=115, y=65)


entry_box = tkinter.Entry(root, width=5, borderwidth=4, relief="groove", font=("Arial", 12))
entry_box.place(x=77, y=100)

entry_box2 = tkinter.Entry(root, width=5, borderwidth=4, relief="groove", font=("Arial", 12))
entry_box2.place(x=133, y=145)


def calculate():
    # sides of the square:
    side1 = entry_box.get() # the entry is giving me str
    side2 = entry_box2.get()

    result = Decimal(side1) * Decimal(side2)
    result_rounded = round(result, 2)
    unit = "m^2"

    label.config(text=(result_rounded, unit))

button2 = tkinter.Button(root, bg="#ededed", borderwidth=3, relief="raised", padx=40, pady=7, font=("Arial", 14), text="Calculate", command=calculate)
button2.place(x=35, y=200)

root.mainloop()









# things that have to change:
# just integers work here. OK
# I want an image of the shape. OK
# need labels directing to the entry boxes
