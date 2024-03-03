# Imports

from guizero import App, Text, PushButton, Picture 
import random

# Variables

list_of_jokes = ["J1", "J2", "J3", "J4", "J5"]

# Functions

def select_joke():
    random_joke = random.randrange(0,len(list_of_jokes)) # selects a random joke number
    joke_message = list_of_jokes[random_joke] # selects the text of the joke from list
    joke_to_display.value = joke_message
   
# App

app = App("Joke Machine", width =700, height=450)
app.bg = "White"
title_text = Text(app, "The Joke Machine")
title_text.text_size = 28
title_text.font = "Impact"

joke_to_display = Text(app, text = "")
joke_to_display.repeat(2000, select_joke) 
button = PushButton(app, command=select_joke, text="Tell me a joke")
joke_to_display = Text(app, text = "")

picture = Picture(app, image="meme.png")

app.display()


