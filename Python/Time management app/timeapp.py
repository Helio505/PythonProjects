# Time management app
# Take time of now, store it, take time of t2, compare, give name to task done

import time
import datetime
from tkinter import *
from tkinter import END
from datetime import datetime
from tkinter import ttk


def dark_mode_toggle():
    root_toggle = Tk()

    def light():
        global dark_mode
        dark_mode = False
        root_toggle.destroy()

    def dark():
        global dark_mode
        dark_mode = True
        root_toggle.destroy()

    button = Button(root_toggle, text="Light mode", padx="20", pady="20", command=light)
    button.grid(row=0, column=0)

    button = Button(root_toggle, text="Dark mode", padx="20", pady="20", command=dark)
    button.grid(row=0, column=1)

    root_toggle.mainloop()
dark_mode_toggle()


# darkmode:
# r_w_c = root_window_color
# e_b_c = entry_box_color
# e_b_2_c = entry_box_time_passed_color
# b_c = buttons_color
# f_c = font color
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
    global time_now
    time_now = time.time()
    return time_now



root = Tk()


root.title("Time management app v2")
# root.geometry("300x320")
root.resizable(width=1, height=0)  #I don't want it to be resizable
root.configure(bg=r_w_c)


entry_box = Entry(root, width=40, bg=e_b_c, fg=f_c_2)
entry_box.grid(row=0, column=0, columnspan=4, padx=8, pady=15)

entry_box_time_passed = Entry(root, width=8, bg=e_b_2_c, fg=f_c_2, relief=RIDGE, borderwidth="1")
entry_box_time_passed.grid(row=2, column=1, padx=15, pady=15)

start_time = 0
finish_time = 0


# These functions are for the stopwatch
def get_name():
    global task_name
    t = entry_box.get()
    task_name = t
    entry_box.delete(0, END)
    entry_box.insert(0, "~~Task was named~~")


def stopwatch_start():
    global state
    state = True

    entry_box.delete(0, END)

    global start_time
    start_time = time.time()

    entry_box.insert(0, "~~started~~")


def stopwatch_finish_calculate():
    # state = False
    entry_box.delete(0, END)

    global finish_time
    finish_time = time.time()

    calc = finish_time - start_time
    round_calc_sec = round(calc, 2) #This controls the rounding
    # display_time = ("Tempo decorrido: " + str(round_calc_sec) + " s")

    # round_calc_sec = round_calc_sec + 26000

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
    
    # display_time = ("Tempo decorrido: ", str(min), " min", str(round_calc_b)" s")

    entry_box.insert(0, display_time)

    date = datetime.now()
    str_date = str(date)
    with open("tasks saved file.txt", "a") as file:
        file.write(str(task_name) + "\n")
        file.write(str_date + "\n")
        file.write(display_time + "\n"*2)

    entry_box.insert(0, "~~ended~~")

    entry_box.update()
    time.sleep(1)
    entry_box.delete(0, 9)

def clear():
    entry_box.delete(0, END)


def update():
    current_time()
    keep_track = time_now - start_time
    keep_track_round = round(keep_track, 2)
    entry_box_time_passed.delete(0, END)
    entry_box_time_passed.insert(0, (str(keep_track_round), "sec"))

def show_file():
    with open("tasks saved file.txt") as file:
        test = file.read()

    root_show_file = Tk()
    root_show_file.geometry("350x600")
    root_show_file.configure(bg=r_w_c)

    textbox = Text(root_show_file, height=30, width=40, bg=r_w_c, fg=f_c, font=14)
    textbox.insert(END, test) # why END?
    textbox.grid(row=1, column=3)

    scrollbar = Scrollbar(root_show_file, orient="vertical", command=textbox.yview)

    scrollbar.grid(row=1, column=4, sticky='ns')

    textbox["yscrollcommand"] = scrollbar.set

    root_show_file.mainloop()


    # labeltest = Label(root, width=40)
    # # labeltest.insert(0, test)
    # labeltest.grid(row=1, column=3)

    # text = Text(labeltest)
    # text.grid(row=1, column=4)

    # spacing_widget = Label(root, width=4, bg=r_w_c)
    # spacing_widget.grid(row=1, column=4)

    # testscroll = Scrollbar(labeltest, command=labeltest)
    # text.config(yscrollcommand=testscroll.set)
    # testscroll.grid(row=1, column=5)
    # labeltest.config(xscrollcommand=testscroll.set)




# Buttons:
button_stopwatch_start = Button(root, text=" Start ", padx=40, pady=20, bg=b_c, fg=f_c, command=lambda: stopwatch_start())

button_stopwatch_finish_calculate = Button(root, text=" Stop ", padx=40, pady=20, bg=b_c, fg=f_c, command=lambda: stopwatch_finish_calculate())

button_get_name = Button(root, text="Name", padx=40, pady=20, bg=b_c, fg=f_c, command=lambda: get_name())

button_clear = Button(root, text=" Clear ", padx=40, pady=20, bg=b_c, fg=f_c, command=lambda: clear())

button_show_time = Button(root, text="Show time", padx=28, pady=20, bg=b_c, fg=f_c, command=lambda: update())

button_show_file = Button(root, text="Show file", padx=28, pady=20, bg=b_c, fg=f_c, command=lambda: show_file())

# button_dark_mode = Button(root, text="Darkmode", padx=28, pady=20, bg=b_c, fg=f_c, command=lambda: dark_mode_toggle())

# Putting the buttons on the screen
button_get_name.grid(row=1, column=0)
button_stopwatch_start.grid(row=2, column=0)
button_stopwatch_finish_calculate.grid(row=3, column=0)
button_clear.grid(row=4, column=0)
button_show_time.grid(row=5, column=0)
button_show_file.grid(row=6, column=0)

# button_dark_mode.grid(row=5, column=1)

root.mainloop()