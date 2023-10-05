# Imports

from guizero import App, Box, Picture, PushButton, Text, TextBox

# Variables


# Functions

def calculate():
    BAEness_value = round(3.25 * ((len(person1_textbox.value)) + (len(person2_textbox.value))))
    result_text.value = (BAEness_value, "%")

    if BAEness_value > 90:
        feedback_text.value = "True BAE"
    elif BAEness_value > 80:
        feedback_text.value = "Top BAE"
    elif BAEness_value > 60:
        feedback_text.value = "Good BAE"
    elif BAEness_value > 40:
        feedback_text.value = "Average BAE"
    elif BAEness_value > 30:
        feedback_text.value = "Potential BAE"
    elif BAEness_value < 30:
        feedback_text.value = "BUST Try using the full name"
    else:
        feedback_text.value = "No Match, try again"
       
def close():
    app.destroy()
    
# App
app = App("Bae  Or Bust", height = 500, width = 420) 
app.bg = "black"
title_text = Text(app, "BAE OR BUST", color = "Pink", size = 32, font = "Impact")

instruction_text = Text(app, "Is the relationship Bae or Bust? Enter two names below", size = 11, color = "Pink")
heart_picture = Picture(app, image="bae.gif")

#text entry
box = Box(app, height = "200", width = "400") 
box.bg = "pink"

person1_textbox = TextBox(box, width = 30, text = "Enter the first name")
person2_textbox = TextBox(box, width=30, text = "Enter the second name")

submit_button = PushButton(app, command = calculate, text='Calculate') # use app as you want the button pink
submit_button.bg = "Pink"

#result
result_text = Text(app, "How BAE", color = "White", size =38)
feedback_text = Text(app, "ARE YOU?", color = "White", size =20) 

close_button = PushButton(app, command = close, text='Close') # use app as you want the button pink  
close_button.bg = "grey" 

app.display()
