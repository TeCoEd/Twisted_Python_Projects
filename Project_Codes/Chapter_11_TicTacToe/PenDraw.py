# Imports

from guizero import App, Box, Drawing, Slider

# Functions

def start(event):
    drawing.last_event = event
    #drawing.first_event = event
   
def draw(event):
    drawing.line(drawing.last_event.x, drawing.last_event.y,event.x, event.y,width=width.value)
    drawing.last_event = event

# App

app = App("Draw", width = 500, height = 520)
banner = Box(app, align="top", width="fill", border=True)
width = Slider(banner, start=1, end=6, align="top")

drawing = Drawing(app, width="fill", height="fill")

drawing.when_left_button_pressed = start
drawing.when_mouse_dragged = draw

app.display()
