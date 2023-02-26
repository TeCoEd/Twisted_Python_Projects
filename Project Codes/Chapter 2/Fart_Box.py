# uses grid layout
# Imports

from guizero import App, Box, Picture, PushButton, Text
import winsound

# Variables


# Functions

def fart_1():
    winsound.PlaySound("Farts/fart1.wav", winsound.SND_ASYNC)

def fart_2():
    winsound.PlaySound("Farts/fart2.wav", winsound.SND_ASYNC)

def fart_3():
    winsound.PlaySound("Farts/fart3.wav", winsound.SND_ASYNC)

def fart_4():
    winsound.PlaySound("Farts/fart4.wav", winsound.SND_ASYNC)

def fart_5():
    winsound.PlaySound("Farts/fart5.wav", winsound.SND_ASYNC)

def fart_6():
    winsound.PlaySound("Farts/fart6.wav", winsound.SND_ASYNC)      
     
# App

app = App("Fart Box", height = "350", width = "350")
app.bg = "Tan"
title_text = Text(app, "F.A.R.T Box")
title_text.text_size = 28
title_text.font = "Impact" # can be any of the following p 16 SEE GUIDE
poo_picture = Picture(app, image="poo.gif")

# Fart buttons
box = Box(app, height = "200", width = "400", layout = "grid")
fart_button1 = PushButton(box, command=fart_1, text='fart 1', grid=[0,0])
fart_button2 = PushButton(box, command=fart_2, text="fart 2", grid=[1,0])
fart_button3 = PushButton(box, command=fart_3, text='fart 3', grid=[2,0])

fart_button4 = PushButton(box, command=fart_4, text='fart 4', grid=[0,1])
fart_button5 = PushButton(box, command=fart_5, text='fart 5', grid=[1,1])
fart_button6 = PushButton(box, command=fart_6, text='fart 6', grid=[2,1])
#fart_button1.bg = "sienna"

#replace with images of poo

#add an leave or close


app.display()


