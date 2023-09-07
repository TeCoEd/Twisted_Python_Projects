# Imports

from guizero import App, Picture, PushButton, Text
import glob
import os

# Variables

global photo_number #photo number
photo_number = 0

# Functions

def forward():
    global photo_number
    global photo
    photo.destroy()
    photo_number = (photo_number + 1) % len(image_file_names)
    photo = Picture(app, image=image_file_names[photo_number])
   
def back():
    global photo_number
    global photo
    photo.destroy()
    photo_number = (photo_number - 1) % len(image_file_names)
    photo = Picture(app, image=image_file_names[photo_number])

def exit(): 
    app.destroy()

def print_to_paper():
    global photo_number
    photo = image_file_names[photo_number]
    print(photo)
    os.startfile(photo, "print")

# App

#image_file_names = [f for f in glob.glob("Photo_Book_Images/*.gif")]
image_file_names = [f for f in glob.glob("O:/OneDrive/Manning Books/CODE/draft code/Photo_Book_Images/*.gif")]

app = App("Photo Album", width=475, height=400)
text = Text(app, text="Photo Book")
album_name = Text(app, text="Some Random Things")

photo = Picture(app, image=image_file_names[photo_number])
back_button = PushButton(app, command=back, text="Previous", align="left")
next_button = PushButton(app, command=forward, text="Next", align="right")
exit_button = PushButton(app, command=exit, text="Close App", align="bottom")
print_button = PushButton(app, command=print_to_paper, text="Print", align="top")

app.display()
