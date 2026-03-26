import datetime as dt
from tkinter import *
from tkcalendar import Calendar

class Main_Function:
    def __init__(self):
        pass
    def open_calendar(self, root):
        calendar_win = Toplevel(root)
        calendar_win.attributes('-topmost', bool(TRUE))
        calendar_win.geometry("250x220")
        calendar_win.resizable(False, False)
        calendar_win.title("Calendar")
        calendar_win.configure(bg="#ffffff")

        date = dt.date.today()
        cal = Calendar(calendar_win,
                       selectmode = 'day',
                       year = date.year, 
                       month = date.month,
                       day = date.day)
        cal.pack(pady=(10))

        cal_btn = Button(calendar_win,
                         text="Select Date")
        cal_btn.pack(fill='x')