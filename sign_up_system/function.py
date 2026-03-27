import datetime as dt
from tkinter import *
from tkcalendar import Calendar
from aset import Aset

class Main_Function:
    def __init__(self):
        self.aset = Aset()
    
    # open calendar function
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

    # select date from calendar function 
    def select_date(self, button):
            self.user_birthdate = self.cal.get_date()
            button.config(text=self.user_birthdate)
            self.calendar_win.destroy()

    # get user data
    def get_user_data(self, fullname_e, email_e, password_e, fullname_l, email_l, password_l, birthdate_l):
        user_fullname = fullname_e.get()
        user_email = email_e.get()
        user_password = password_e.get()

        # warn entry class to tell that entry is empty
        try:
            class warn_entry:
                def __init__(self, entry_value, title_label, text_label):
                    self.aset = Aset()
                    self.entry_val = entry_value
                    self.title_label = title_label
                    self.text_label = text_label
                def empty_warn(self):
                    if self.entry_val != "":
                        self.title_label.config(image="", text=self.text_label)
                    else:
                        self.title_label.config(image=self.aset.red_dot, compound="left", text=self.text_label)
                        self.title_label.image = self.aset.red_dot

            fullname_warn = warn_entry(user_fullname, fullname_l, "Full name :")
            fullname_warn.empty_warn()

            fullname_warn = warn_entry(user_email, email_l, "Email :")
            fullname_warn.empty_warn()
            

            fullname_warn = warn_entry(user_password, password_l, "Password")
            fullname_warn.empty_warn()

            if self.user_birthdate:
                birthdate_l.config(image="", text="Date of birth :")

        except AttributeError:
            birthdate_l.config(image=self.aset.red_dot, compound="left", text="Date of birth :")
            birthdate_l = self.aset.red_dot

