# Imports

from guizero import App, info, Text, TextBox, PushButton 

# Variables

# Functions
def PasswordCheck():
    password = password_textbox.value
    if (len(password)<8):
        app.error("Length ", "Your password must be at least 8 characters long")
        
    elif not any(x.islower() for x in password):
        app.error("Lower Case ", "Your password must include at least one lowercase letter")
                          
    elif not any(x.isupper() for x in password):
        app.error("Upper Case ", "Your password must include at least one capital letter")
        
    elif not any(x.isdigit() for x in password):
        app.error("Number ", "Your password must include at least one number")
        
    else:
        app.info("SECURE", "*** YOUR PASSWORD IS SECURE ***")
    
  
# App
app = App("Password Strength Checker", width =700, height=300)
app.bg = "White"
title_text = Text(app, "Password Strength Checker")
title_text.text_size = 28
title_text.font = "Impact"

#enter text
instruction = Text(app, text="Enter your Password Below")
password_textbox = TextBox(app, width=50)

#button
button = PushButton(app, command=PasswordCheck, text="Check Password")

app.display()
