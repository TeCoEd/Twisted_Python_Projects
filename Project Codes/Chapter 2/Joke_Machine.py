# Imports

from guizero import App, Text, PushButton 
import random

# Variables

list_of_jokes = ["What do you call a man with no shins? Tony (Toe – Knee)",
                 "Nothing begins with N and ends with G",
                 "What kind of tree can fit in one hand? Palm tree",
                 "Why do owls not go dating in the rain? Because it’s too wet to woo"]

print (list_of_jokes)

# Functions

def select_joke():
    random_joke = random.randrange(0,len(list_of_jokes)) # selects a random joke number
    joke_message = list_of_jokes[random_joke] # selects the text of the joke from list
    joke_to_display.value = joke_message
    
     
# App

app = App("Joke Machine", width =700, height=300)
app.bg = "White"
title_text = Text(app, "The Joke Machine")
title_text.text_size = 28
title_text.font = "Impact" 
button = PushButton(app, command=select_joke, text="Tell me a joke")
joke_to_display = Text(app, text = "")

app.display()

