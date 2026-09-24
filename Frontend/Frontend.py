
# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import datetime

# Create Object
root = Tk()

# Set geometry
root.geometry("800x800")


#Obtin ziua de astazi 
current_date = datetime.now()
# Add Calendar
cal = Calendar(root, selectmode = 'day',
               year = current_date.year, month = current_date.month,
               day = current_date.day,maxdate = current_date,showothermonthdays = False)

cal.pack(pady = 20)

def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())

# Add Button and Label
Button(root, text = "Get Date",
       command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)

# Execute Tkinter
root.mainloop()



