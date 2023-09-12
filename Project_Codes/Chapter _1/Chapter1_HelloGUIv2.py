# Imports

from guizero import App, info, PushButton, TextBox, Text

# Variables


# Functions

def Hello():
    app.warn("Welcome", "Hello " + textbox.value + ", you just made your first GUI")

# App    

app = App("Hello World", bg = "red")
text = Text(app, text="Enter your name")
textbox = TextBox(app, width=40)
button = PushButton(app, command=Hello, text="Click me", )
app.display()
