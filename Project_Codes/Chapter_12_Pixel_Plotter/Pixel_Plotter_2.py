 # Imports

from guizero import App, Waffle, Text, PushButton
import random

# Variables

colors = ["red", "blue", "green", "yellow", "magenta", "purple", "white", "black", "orange", "pink", "brown"]
board_size = 15 
global currentX
global currentY
currentX = 0
currentY = 0

# Functions

def clear_board():
    global currentX
    global currentY
    delete_button.disable()
    for x in range(board_size):
        for y in range(board_size):
            board.set_pixel(x, y, color = "white")
        currentX = 0
        currentY = 0
            
def delete_last_pixel():
    global currentX
    global currentY
    
    # Checks which pixel to delete
    if currentX == 1:
        delete_button.disable()
        board.set_pixel(currentX-1, currentY, color = "white")
        currentX = currentX - 1 
    elif currentX == 0:
        currentX += (board_size - 1)
        currentY -= 1
        board.set_pixel(currentX, currentY, color = "white")
    else:
        delete_button.enable()
        currentX -= 1
        board.set_pixel(currentX, currentY, color = "white")
        
              
def create_palette():
    for color in colors:
        palette.set_pixel(colors.index(color), 0, color)

def fill(x, y, target, color):
    board.set_pixel(x, y, color)        
       
def color_pixel(x, y):
    global currentX
    global currentY
    delete_button.enable() 
    color = palette.get_pixel(x,y)
    target = board.get_pixel(currentX,currentY)
    fill(currentX, currentY, target, color)
    if currentX < board_size -1:
        currentX += 1
    else:
        currentY += 1
        currentX = 0

def close_app(): 
    app.info("Pixel Plotter", "See you again!") 
    app.destroy() 
    
# App

app = App("Pixel Plotter", width = ((board_size * 25) + 90), height = ((board_size * 22) + 240)) 

title_text = Text(app, "PIXEL PLOTTER")
title_text.text_size = 20
title_text.font = "Consolas"

board = Waffle(app, width=board_size, height=board_size, pad=2)
palette = Waffle(app, width=len(colors), height=1, dotty=True, command=color_pixel) 
clear_button = PushButton(app, command=clear_board, text="Clear Pixels")
delete_button = PushButton(app, command=delete_last_pixel, text="Delete Last Pixel")
close_button = PushButton(app, text="CLOSE APP", command=close_app) 
close_button.bg = "orange red" 

create_palette()

app.display()
