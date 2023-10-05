# Imports

from guizero import App, Box, Picture, PushButton, Text, TextBox

# Variables

# Functions

def calculate():
    BAEness_value = round(3.25 * ((len(person1_textbox.value)) + (len(person2_textbox.value))))
    result_text.value = (BAEness_value, "%")
    
# App

app = App("Bae  Or Bust", height = 400, width = 420)
app.bg = "black"
title_text = Text(app, "BAE OR BUST", color = "Pink", size = 28, font = "Impact")

instruction_text = Text(app, "Is the relationship Bae or Bust? Enter two names below", size = 11, color = "Pink")
heart_picture = Picture(app, image="bae.gif")

# text entry
box = Box(app, height = "200", width = "400")
box.bg = "pink"

person1_textbox = TextBox(box, width = 30, text = "Enter the first name")
person2_textbox = TextBox(box, width=30, text = "Enter the second name")

submit_button = PushButton(app, command = calculate, text='Calculate') # use app as you want the button pink
submit_button.bg = "Pink"

#result
result_text = Text(app, "", color = "White", size =40)

app.display()


