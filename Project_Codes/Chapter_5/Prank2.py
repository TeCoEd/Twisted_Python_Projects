# Imports

from guizero import App, Box, Text, PushButton, Picture 
from random import choice
from time import sleep
import winsound

# Variables

colors = ("yellow", "green", "pink", "white", "orange")


# Functions

def prank_me_play_music():
    winsound.PlaySound("Rick.wav", winsound.SND_ASYNC)
    app.bg = choice(colors)

    #shows a picture of rick
    sleep(2)
    rick_pic = Picture(app, image="rick_dance.gif")

    title_text = Text(answer_grid, "   YOU GOT RICK ROLLED"   , grid =[0, 0])
    title_text.text_size = 18
    score_text = Text(answer_grid, "  Your current score = ricked  ", grid =[0, 7])
    
    ricked_again()

def ricked_again():
    prank_again = app.yesno("Rick Rolled", "Want to be Rick Rolled again?")
    if prank_again == True:
        app.info("Rick says", "Never gonna give you up!")
        prank_me_play_music()
    else:
        app.error("Rick says", "I let you down...")
        app.destroy()
# App

app = App("General Knowledge Quiz", width=330, height=388)
your_name = app.question("The Quiz", "What's your name?")
answer_grid = Box(app, layout = "grid")
title_text = Text(answer_grid, "Q1: Which food do I not like?", grid =[0, 0])
score_text = Text(answer_grid, your_name + "'s current score = 0", grid =[0, 7])
title_text.text_size = 14
title_text.font = "Comic Sans"

answer1= PushButton(answer_grid, command=prank_me_play_music, text='Pasta', grid =[0, 2])
answer2= PushButton(answer_grid, command=prank_me_play_music, text='Hot Dog', grid =[0, 4])
answer3= PushButton(answer_grid, command=prank_me_play_music, text='Sandwich', grid =[0, 6])

app.display()




