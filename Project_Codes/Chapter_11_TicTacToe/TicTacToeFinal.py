# Imports

from guizero import App, Drawing, Slider, Combo, Box, Text, PushButton, Window
import sys
from time import sleep

# Functions

def build_grid():
    # create the grid - down
    drawing.rectangle(150, 25, 140, 450, color="blue")
    drawing.rectangle(340, 25, 350, 450)

    # create the grid - across
    drawing.rectangle(20, 140, 480, 155)
    drawing.rectangle(20, 310, 480, 325)
    
def start(event):
    drawing.last_event = event
    #drawing.first_event = event
   
def draw(event):
    drawing.line(drawing.last_event.x, drawing.last_event.y,event.x, event.y,width=width.value,color=color.value)
    drawing.last_event = event

def restart_game():
    command=drawing.clear()
    build_grid()

def close_app():
    app.info("Tic Tac Toe", "Thanks for playing")
    sleep(0.5)
    app.destroy()
    sys.exit()
    
# App

app = App("TicTacToe", width = 525, height = 690)

# title
title_grid = Box(app, align="top", width="fill", border=True)
title = Text(title_grid, size =35, font="Helvetica",text = "Tic-Tac-Toe")
title_grid.bg = "white"

#toolbox

toolbox = Box(app, align="top", width="400", border=True)
toolbox.bg ="white"

color_heading = Text(toolbox, text="Color", align="top")
color = Combo(toolbox, options=["black", "white", "red", "blue"], align="top")

width_label = Text(toolbox, text="Width", align="top")
width = Slider(toolbox, start=3, end=6, align="top")

new_game = PushButton(toolbox, text="New Game", command=restart_game, align="left") ## clears all
close_button = PushButton(toolbox, text="Close App", command=close_app, align="right")

#game grid

drawing = Drawing(app, width="fill", height="fill")
build_grid()

# drawing

drawing.when_left_button_pressed = start
drawing.when_mouse_dragged = draw

app.display()
