from time import strftime
import tkinter as tk
#from datetime import datetime


# Creating main window
window=tk.Tk()
window.title("Digital Clock")

# Updating Time and Date
def update_time_and_date() :

    ongoing_time=strftime(' %H:%M:%S ') # Pulling Current Time
    #ongoing_time=datetime.now().strftime("%H:%M:%S") # Pulling Current Time using datetime module
    present_date=strftime(' %d %B %Y,%A ')  # Pulling current date
    time_label.config(text=ongoing_time)
    date_label.config(text=present_date)
    time_label.after(1000,update_time_and_date)  # Updating Every Second

# Displaying Date
date_label=tk.Label(
    window, 
    font=("Arial",40), 
    background="black", 
    foreground="yellow"
)
date_label.pack(anchor="center")

# Displaying Time
time_label=tk.Label(
    window, 
    font=("Arial",40), 
    background="black", 
    foreground="red"
)
time_label.pack(anchor="center")

# Start the clock
update_time_and_date()

# Run the application
window.mainloop()
