"""
    Clock that updates each second.

    Information:
        - tkinter
        - time
        - GUI
"""

from tkinter import *
from time import strftime

root = Tk()
root.configure(background="#333333")

label = Label(root, padx=32, pady=20, font=16,
              background="#333333", foreground="white")
label.grid(row=0, column=0)

def show_time():
    clock = strftime('%H:%M:%S %p')
    label.config(text=clock)
    label.after(1000, show_time) # .after uses miliseconds

button = Button(root, text="Show", padx=40, pady=16,
                background="#333333", foreground="white", command=show_time)
button.grid(row=1, column=0)

root.mainloop()