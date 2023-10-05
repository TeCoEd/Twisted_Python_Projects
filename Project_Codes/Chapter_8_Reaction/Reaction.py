# Imports

from guizero import App, Text, Picture, PushButton, info
import random
from time import sleep

# Variables

    
# Functions

def start():
    #print ("start")
    #sleep(random.random() + random.random() + 1)
    sleep(random.uniform(0.5,3.0))
    button2.bg="Green"
    final_time.repeat(10, timer) # Edit to speed

def timer():
    final_time.value = int(final_time.value) + 1

def stop():
    final_time.cancel(timer)
    #print ("Your time was", final_time) # add final time
    reaction_speed  = float(final_time.value) / 45
    reaction_speed = "{:.5f}".format(reaction_speed)
    app.info("Your reaction time ", "Your reaction time was " + str(reaction_speed) + " seconds")

    #reset the game
    
    play_again = app.yesno("Reaction", "Do you want to try again?")
    if play_again == True:
        app.info("Reaction", "Press the start button to begin")
        button2.bg="orange"
        final_time.value = 0
    else:
        app.warn("Reaction", "Thanks for playing, now to save the world!")
        app.destroy()    
    
# App

app = App("Reaction Timer", bg="white")

title_text = Text(app, "Are you faster than a Superhero?")
title_text.text_size = 20
title_text.font = "Comic Sans"

instruction_text = Text(app, "Press Start to begin. Click the orange box when it turns green?")
instruction_text.text_size = 12
instruction_text.font = "Comic Sans"

superhero_logo = Picture(app, image="superhero.png")

button1 = PushButton(app, command=start, width=20, height=2, text='Start')
button1.text_size = 10

button2= PushButton(app, command=stop, width=20, height=4, text='Press When Green')
button2.bg="orange"

final_time = Text(app, text = "0")
#final_time.text_color = "white" #for testing

app.display()

