import tkinter
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("Image viewer")

def select_files():
    """
        - Selects the image.
        - Opens the image.
        - Converts the image to tkinter readable format.
        - Displays the image.
    """

    filename = askopenfilename()

    global image_opened
    image_opened = Image.open(filename)

    global tk_image
    tk_image = ImageTk.PhotoImage(image_opened)

    global label
    label_showing_image = tkinter.Label(root, image=tk_image)
    label_showing_image.grid(row=0, column=0)

rotation_step = 0
def rotate_image():
    """
        - Rotates the image 90 degrees on each click.
        - Displays the image after rotation.
    """
    global rotation_step
    rotation_step += 90

    image_opened_rotation = image_opened

    image_rotated = image_opened_rotation.rotate(rotation_step)

    global tk_image_rotated
    tk_image_rotated = ImageTk.PhotoImage(image_rotated)

    label_showing_image_rotated = tkinter.Label(root, image=tk_image_rotated)
    label_showing_image_rotated.grid(row=0, column=0)

    if rotation_step >= 360:
        rotation_step = 0

button_select_files = tkinter.Button(root, padx=40, pady=10, text="File", command=select_files)
button_select_files.grid(row=1, column=0)

button_rotate = tkinter.Button(root, padx=40, pady=10, text="Rotate", command=rotate_image)
button_rotate.grid(row=2, column=0)

root.mainloop()