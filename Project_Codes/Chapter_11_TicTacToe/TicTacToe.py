# Imports

from guizero import App, Drawing, Slider, Box, Text

# Functions

def start(event):
    drawing.last_event = event
    #drawing.first_event = event
   
def draw(event):
    drawing.line(drawing.last_event.x, drawing.last_event.y,event.x, event.y,width=width.value)
    drawing.last_event = event

# App

app = App("TicTacToe", width = 500, height = 520)
app.font = "Calibri"
banner = Box(app, align="top", width="fill", border=True)
width = Slider(banner, start=1, end=6, align="top")

drawing = Drawing(app, width="fill", height="fill")

# create the grid - down
drawing.rectangle(150, 25, 140, 450)
drawing.rectangle(340, 25, 350, 450)

# create the grid - across
drawing.rectangle(20, 140, 480, 155)
drawing.rectangle(20, 310, 480, 325)

drawing.when_left_button_pressed = start
drawing.when_mouse_dragged = draw

app.display()
