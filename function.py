import datetime as dt
from tkinter import *
from tkcalendar import Calendar

class Main_Function:
    def __init__(self):
        pass

    def open_calendar(self, root, button):
        self.calendar_win = Toplevel(root)
        self.calendar_win.attributes('-topmost', bool(TRUE))
        self.calendar_win.geometry("250x220")
        self.calendar_win.resizable(False, False)
        self.calendar_win.title("Calendar")
        self.calendar_win.configure(bg="#ffffff")

        date = dt.date.today()
        self.cal = Calendar(self.calendar_win,
                       selectmode = 'day',
                       year = date.year, 
                       month = date.month,
                       day = date.day)
        self.cal.pack(pady=(10))

        self.cal_btn = Button(self.calendar_win,
                         text="Select Date",
                         command=lambda: self.select_date(button))
        self.cal_btn.pack(fill='x')

    def select_date(self, button):
        button.config(text=self.cal.get_date())
        self.calendar_win.destroy()