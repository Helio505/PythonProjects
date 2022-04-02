# Time tracking/management app

import time
import datetime
from tkinter import *
from tkinter import END
from datetime import datetime
from tkinter import ttk
from decimal import Decimal

# Dark mode choice window:
def dark_mode_toggle():
    """Returns the value of dark_mode,
     so that it is applied according to the choice"""
    root_toggle = Tk()
    root_toggle.geometry("150x150")

    def light():
        global dark_mode
        dark_mode = False
        root_toggle.destroy()

    def dark():
        global dark_mode
        dark_mode = True
        root_toggle.destroy()

    button = Button(root_toggle, text="Light mode", padx="18.7", pady="20", command=light)
    button.place(x=20, y=10)

    button2 = Button(root_toggle, text="Dark mode", padx="20", pady="20", command=dark)
    button2.place(x=20, y=80)

    root_toggle.mainloop()
dark_mode_toggle()

if dark_mode == True:
    r_w_c = "#4d4d4d"
    e_b_c = "#c7c7c7"
    e_b_2_c = "#757575"
    b_c = "#595959"
    f_c = "white"
    f_c_2 = "black"
else:
    r_w_c = "white"
    e_b_c = "white"
    e_b_2_c = "white"
    b_c = "white"
    f_c = "black"
    f_c_2 = "black"


time_now = 0
def current_time():
    """When it is called, it returns the current time in seconds. It is isolated
    to remove interference from local tkinter stuff."""
    global time_now
    time_now = time.time()
    return time_now


# Main window:
root = Tk()

root.title("Time management app v2")
root.geometry("500x350")
# root.resizable(width=1, height=0)
root.configure(bg=r_w_c)

# Entry to receive the name, and display the time:
entry_box = Entry(root, width=45, bg=e_b_c, fg=f_c_2)
entry_box.place(x=175, y=20)

# Entry to display current time passed:
entry_box_time_passed = Entry(root, width=10, bg=e_b_2_c, fg=f_c_2, relief=RIDGE, borderwidth="1")
entry_box_time_passed.place(x=280, y=240)

start_time = 0
finish_time = 0


# These functions are for the stopwatch
def get_name():
    """This func gets the name of the task,
     if the task doesn't have a name stuff breaks."""
    global task_name
    t = entry_box.get()
    task_name = t
    entry_box.delete(0, END)
    entry_box.insert(0, "~~Task was named~~")


def stopwatch_start():
    """Starts the stopwatch"""
    global state
    state = True

    entry_box.delete(0, END)

    global start_time
    start_time = time.time()

    entry_box.insert(0, "~~started~~")


def stopwatch_finish_calculate():
    """Stops the stopwatch and calculates t1-t0. Also converts everything to
    a format tkinter understands."""
    # state = False
    entry_box.delete(0, END)

    global finish_time
    finish_time = time.time()

    calc = finish_time - start_time
    round_calc_sec = round(calc, 2) 

    # These if statements and while loops are for the conversion from seconds, to
    # minutes, hours, etc.

    # For seconds:
    if round_calc_sec < 60:
        display_time = ("Tempo decorrido: " + str(round_calc_sec) + " sec")

    # For minutes:
    min = 0
    while round_calc_sec >= 60:
        min = min + 1
        round_calc_sec -= 60

        round_calc_b = round(round_calc_sec, 2)
        display_time = f"Tempo decorrido: {str(min)} min {str(round_calc_b)} s"

    # For hours:
    hour = 0
    while min >= 60:
        hour += 1
        min -= 60
        round_calc_sec -= 60
        display_time = f"Tempo decorrido: [{str(hour)} h / {str(min)} min / {str(round_calc_b)} s]"
    
    entry_box.insert(0, display_time)

    # These lines of code are inserting the values into the .txt file:
    creation_date = datetime.now()
    creation_str_date = str(creation_date)
    with open("tasks saved file.txt", "a") as file:
        file.write(str(task_name) + "\n")     # Task name
        file.write(creation_str_date + "\n")  # When task was created 
        file.write(display_time + "\n"*2)     # Time spent doing the task

    # Simple feedback:
    entry_box.insert(0, "~~ended~~")
    entry_box.update()
    time.sleep(1)
    entry_box.delete(0, 9)


# Just deletes stuff so that you can add another task:
def clear():
    entry_box.delete(0, END)

def testing():
    print("here here here here")

def update():
    """Shows the current time passed since the start of the stopwatch.
    It exists because if it didn't you would have to save the task to database to
    see the time, but with this you can see with no influence on other stuff."""
    current_time()
    keep_track = time_now - start_time
    keep_track_round = round(keep_track, 2)
    entry_box_time_passed.delete(0, END)
    entry_box_time_passed.insert(0, (str(keep_track_round), "sec"))


def show_file():
    "Opens in a new window, the file where the tasks are stored."
    with open("tasks saved file.txt") as file:
        test = file.read()

    root_show_file = Tk()
    root_show_file.geometry("350x600")
    root_show_file.configure(bg=r_w_c)

    # Somehow this scroll feature works, don't change anything here:
    textbox = Text(root_show_file, height=30, width=40, bg=r_w_c, fg=f_c, font=14)

    textbox.insert(END, test) # why END?
    textbox.grid(row=1, column=3)

    scrollbar = Scrollbar(root_show_file, orient="vertical", command=textbox.yview)

    scrollbar.grid(row=1, column=4, sticky='ns')

    textbox["yscrollcommand"] = scrollbar.set

    root_show_file.mainloop()


# Buttons:
button_stopwatch_start = Button(root, text=" Start ", padx=40, pady=20, bg=b_c, fg=f_c, command=lambda: stopwatch_start())

button_stopwatch_finish_calculate = Button(root, text=" Stop ", padx=40, pady=20, bg=b_c, fg=f_c, command=lambda: stopwatch_finish_calculate())

button_get_name = Button(root, text="Name", padx=40, pady=20, bg=b_c, fg=f_c, command=lambda: get_name())

button_clear = Button(root, text=" Clear ", padx=40, pady=20, bg=b_c, fg=f_c, command=lambda: clear())

button_show_time = Button(root, text="Show time", padx=28, pady=20, bg=b_c, fg=f_c, command=lambda: update())

button_show_file = Button(root, text="Show file", padx=28, pady=20, bg=b_c, fg=f_c, command=lambda: show_file())

# button_test = Button(root, text="Test", padx=32, pady=20, bg=b_c, fg=f_c, command=lambda: test())

# Putting the buttons on the screen
button_get_name.place(x=2, y=60)
button_stopwatch_start.place(x=2, y=130)
button_stopwatch_finish_calculate.place(x=0, y=200)
button_clear.place(x=125, y=270)
button_show_time.place(x=250, y=270)
button_show_file.place(x=375, y=270)
# button_test.place(x=500, y=270)


root.mainloop()