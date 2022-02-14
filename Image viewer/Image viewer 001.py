import tkinter
from PIL import Image, ImageTk
# from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = tkinter.Tk()
# properties of window:
root.title("Image viewer 001")


global k #k means keepTrack #it had the name of i
k = 0

def select_files():
    filename = askopenfilename()

    global imageOpened
    imageOpened = Image.open(filename)

    global tkimage
    tkimage = ImageTk.PhotoImage(imageOpened)

    global label
    label = tkinter.Label(root, image=tkimage)
    label.grid(row=0, column=0)

def rotate_image():
    global imageOpened_test
    imageOpened_test = imageOpened
    continuous_rotation()

def continuous_rotation():  #this function executes each time you click the button rotate, each time it will rotate 90 degrees
    global k
    k = k + 1
    print(k)
    if k == 1:
        print("z1")
        test1 = imageOpened_test.rotate(90)

        global tkimage1
        tkimage1 = ImageTk.PhotoImage(test1)
        label = tkinter.Label(root, image=tkimage1)
        label.grid(row=0, column=0)

    if k == 2:
        print("z2")
        test2 = imageOpened_test.rotate(180)

        global tkimage2
        tkimage2 = ImageTk.PhotoImage(test2)
        label = tkinter.Label(root, image=tkimage2)
        label.grid(row=0, column=0)

    if k == 3:
        print("z3")
        test3 = imageOpened_test.rotate(270)

        global tkimage3
        tkimage3 = ImageTk.PhotoImage(test3)
        label = tkinter.Label(root, image=tkimage3)
        label.grid(row=0, column=0)

    if k == 4:
        print("z4")
        test4 = imageOpened_test.rotate(360)

        global tkimage4
        tkimage4 = ImageTk.PhotoImage(test4)
        label = tkinter.Label(root, image=tkimage4)
        label.grid(row=0, column=0)
        k = 0  #this is restarting my loop

button_selectFiles = tkinter.Button(root, padx=40, pady=10, text="Files", command=select_files)
button_selectFiles.grid(row=1, column=0)

button_rotate = tkinter.Button(root, padx=40, pady=10, text="Rotate", command=rotate_image)
button_rotate.grid(row=2, column=0)

root.mainloop()
