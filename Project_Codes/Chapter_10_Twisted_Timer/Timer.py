# Imports

from guizero import App, PushButton, Slider, Text, TextBox

# Variables

slider_step_value = 1 
global total_seconds

# Functions

def slider_changed_hour(slider_step_value): 
    textbox_hour.value = slider_step_value 

def slider_changed_minute(slider_step_value): 
    textbox_minute.value = slider_step_value 

def slider_changed_second(slider_step_value): 
    textbox_second.value = slider_step_value 

def initialize_countdown(): 
    global total_seconds
    hours = int(textbox_hour.value)
    minutes = int(textbox_minute.value)
    seconds = int(textbox_second.value) 
    
    total_seconds = ((hours * 3600) + (minutes * 60) + seconds)

    # calculate time and display
    i = total_seconds
    total_time = str(f"{i//3600:02d}:{(i%3600)//60:02d}:{i%60:02d}")
    time_left.value = (total_time) 
       
    start_button.bg = "#bff000" 
    restart_button.disable() 

def begin_countdown():
    time_left.repeat(1000, countdown) 
    
def countdown(): 
    global total_seconds
    
    time_left.value = total_seconds 
    i = total_seconds
    
    total_time = str(f"{i//3600:02d}:{(i%3600)//60:02d}:{i%60:02d}")
    time_left.value = (total_time) 
    total_seconds = total_seconds - 1

    if total_seconds > 0:
        pass
    elif total_seconds < 0:
        time_left.cancel(countdown) 
        app.bg = "red"
        time_left.value = ("TIME'S UP")
        #total_seconds = 0 # reset the time to 0
        restart_button.bg ="#EBECF0"
        restart_button.enable()

def reset_countdown(): 
    app.bg =" #EBECF0" 
    submit_button.bg ="orange"
    time_left.value = "00:00:00"
    
# App

app = App("Countdown Timer", height = 610 )
app.bg =" #EBECF0" 
title_label = Text(app, size = 25, text = "COUNTDOWN TIMER")

instruct1 = Text(app, "Use the sliders to select hours, minutes and seconds")
instruct2 = Text(app, "Press the ORANGE submit button when ready")
instruct3 = Text(app, "Press the GREEN button to begin the countdown")
instruct4 = Text(app, "")

#Hours
hour_title = Text(app, "HOURS")
slider_hour = Slider(app, width = 200, height = 22, start=0, end=4, command=slider_changed_hour)
textbox_hour = TextBox(app, "0" )
textbox_hour.hide() # hides the saved numbers 


#Minutes
minute_title = Text(app, "MINUTES")
slider_minute = Slider(app, width = 200, height = 22, start=0, end=59, command=slider_changed_minute)
textbox_minute = TextBox(app, "0" )
textbox_minute.hide() 

#Seconds
second_title = Text(app, "SECONDS")
slider_second = Slider(app, width = 200, height = 22, start=0, end=59, command=slider_changed_second)
textbox_second = TextBox(app, "0" )
textbox_second.hide() 

#submit button
submit_button = PushButton(app, command = initialize_countdown, text="Submit") 
submit_button.bg ="orange"

#Start
start_button = PushButton(app, command = begin_countdown, text="Start Countdown") 

remaing_time_label = Text(app, "TIME REMAINING")
time_left = Text(app, size = 50, text = "00:00:00")

restart_button = PushButton(app, command = reset_countdown, text="Reset Countdown") 
restart_button.disable()
                 
app.display()
