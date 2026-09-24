from tkinter import *
from tkcalendar import Calendar
from datetime import datetime

class CalendarInit():
    current_date = datetime.now()

    def __init__(self, fereastra):
        self.cal = Calendar(fereastra, selectmode = 'day',
               year = self.current_date.year, month = self.current_date.month,
               day = self.current_date.day,maxdate = self.current_date,showothermonthdays = False)

        self.cal.pack(pady = 20)



## mic test

#fereastra noua 

root = Tk()
root.geometry("400x400")


calendar = Calendar() 
root.mainloop()


## SOURCE: https://www.geeksforgeeks.org/python/create-a-date-picker-calendar-tkinter/
## SOURCE: https://www.geeksforgeeks.org/python/get-current-date-using-python/