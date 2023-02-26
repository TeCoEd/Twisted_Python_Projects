# Imports

from guizero import App, Picture, PushButton, Text
import glob

# Variables

global Pnum #photo number
Pnum = 0

# Functions

def forward():
    global Pnum
    global photo
    photo.destroy()
    photo = Picture(app, image=image_file_names[Pnum])
    Pnum = Pnum + 1
    if Pnum == len(image_file_names): 
        Pnum = 0
    
def back():
    global Pnum
    global photo
    photo.destroy()
    photo = Picture(app, image=image_file_names[Pnum])
    Pnum = Pnum - 1
    if Pnum == -1: 
        Pnum = + len(image_file_names)-1                          

def exit():
    app.destroy()
    
# App    
image_file_names = [f for f in glob.glob("Photo_Book_Images/*.gif")] # FIND IN A FOLDER
#print (image_file_names)

app = App("Photo Album", width = 475, height = 400)
text = Text(app, text="Photo Book")
album_name = Text(app, text="Some Random Things")

photo = Picture(app, image="Photo_Book_Images/one.gif")
back_button = PushButton(app, command = back, text = "Previous", align="left")
next_button = PushButton(app, command = forward, text ="Next", align="right")
exit_button = PushButton(app, command = exit, text ="Close App", align="bottom")

app.display()

# change the backgound color
# chnage colour of the buttons
