# Imports

from guizero import App, Box, Picture, PushButton, Text 
from random import randint
from time import sleep
#import sys 

# Variables

global lives
lives = 5


# Functions

def check_the_guess():
    global lives
    number = randint(1,1)
    
    while lives > 0:
        
        guess = app.question("Guess", "Mortal, enter the number I am thinking of")

        lives_left_text.value = lives - 1
        
        if int(guess) > number:
            app.error("Lower", "Poor effort, the number is lower")
            lives = lives - 1
        elif int(guess) < number:
            app.warn("Higher", "No fool, try a higher number")
            lives = lives - 1
        else:
            app.info("Well done", "Mortal, you win!")
            play_again()
                
    app.error("Lost", "You have failed my pretty, the number was " + str(number))
    sleep(0.5)
    app.destroy()

def play_again():
    global lives
    play_again = app.yesno("Witch", "Do you want to try again mortal?")
    if play_again == True:
        lives_left_text.value = 5
        lives = 5
        app.info("Witch", "Excellent choice!")
        check_the_guess()
        
    elif play_again == False:    
        app.info("Witch", "A wise choice...")
        sleep(1)
        app.destroy()
        #sys.exit() 

    else:
        pass
    
# App

app = App("Guess the Number", height = 400, width = 350)
title_text = Text(app, "Can you guess my secret number?")
title_text.text_size = 16
title_text.font = "Impact" 

pic = Picture(app, image="witch.gif")

lives_heading = Text(app, "Lives Left")
lives_left_text = Text(app, lives)
lives_left_text.text_size = 42

begin_button = PushButton(app, command=check_the_guess, width=20, height=2, text='Click to begin')
begin_button.text_size = 10

app.display()
