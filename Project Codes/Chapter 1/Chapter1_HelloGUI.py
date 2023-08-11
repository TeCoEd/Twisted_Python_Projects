# Imports

from guizero import App, info, PushButton, TextBox, Text

# Variables


# Functions

def Hello():
    info("Welcome", "Hello " + textbox.value + ", you just made your first GUI")

# App    

app = App("Hello World")
text = Text(app, text="Enter your name")
textbox = TextBox(app, width=20)
button = PushButton(app, command=Hello, text="Click me", )
app.display()
