from tkinter import *
from datetime import datetime as dt
import csv
from tkcalendar import Calendar
from aset import Aset

class Main_Function:
    def __init__(self):
        self.aset = Aset()
        self.user_data = {'Full name' : [], 'Gender' : [], 'Date of birth' : [], 'Email' : [], 'Password' : []}
    
    # open calendar function
    def open_calendar(self, root, open_calendar_button):
        self.calendar_win = Toplevel(root)
        self.calendar_win.attributes('-topmost', bool(TRUE))
        self.calendar_win.geometry("250x220")
        self.calendar_win.resizable(False, False)
        self.calendar_win.title("Calendar")
        self.calendar_win.configure(bg="#ffffff")

        # date = dt.now()
        self.cal = Calendar(self.calendar_win)
        self.cal.pack(pady=(10))

        self.cal_btn = Button(self.calendar_win,
                         text="Select Date",
                         command=lambda: self.select_date(open_calendar_button))
        self.cal_btn.pack(fill='x')

    # select date from calendar function 
    def select_date(self, select_date_button):
            self.user_birthdate = str(dt.strptime(str(self.cal.get_date()), "%m/%d/%y").date())
            select_date_button.config(text=self.user_birthdate)
            self.calendar_win.destroy()

    # get fullname and password
    def get_name_pass(self, fullname_entry, fullname_label, password_entry, password_label):
        self.user_fullname = fullname_entry.get()
        self.user_password = password_entry.get()

        self.name_and_password_status = False
        name_status = False
        password_status = False

        class warn_entry:
            def __init__(self, entry_value, title_label, text_label, status):
                self.aset = Aset()
                self.entry_val = entry_value
                self.title_label = title_label
                self.text_label = text_label
                self.status = status
            def empty_warn(self):
                if self.entry_val != "":
                    self.title_label.config(image="", text=self.text_label)
                    self.status = True
                else:
                    self.title_label.config(image=self.aset.red_dot, compound="left", text=self.text_label)
                    self.title_label.image = self.aset.red_dot
                    self.status = False
        
        fullname_warn = warn_entry(self.user_fullname, fullname_label, "Full name :", name_status)
        fullname_warn.empty_warn()

        password_warn = warn_entry(self.user_password, password_label, "Password :", password_status)
        password_warn.empty_warn()

        if fullname_warn.status == True and password_warn.status == True:
            self.name_and_password_status = True
            print("name and password have been filled in")

    # get user gender
    def get_user_gender(self, selected_gender, gender_title):
        self.user_gender = selected_gender.get()
        self.gender_status = False
        if self.user_gender == "":
            gender_title.config(text="Gender :", image=self.aset.red_dot, compound='left')
            self.gender_status = False
        else:
            gender_title.config(text="Gender :", image='')
            self.gender_status = True
            print("gender have been filled in")

    # get user date of birth
    def get_birth_date(self, birthdate_label):
        self.date_status = False
        try:
            if self.user_birthdate:
                birthdate_label.config(image="", text="Date of birth :")
                self.date_status = True
            else:
                return None
            
        except AttributeError:
            birthdate_label.config(image=self.aset.red_dot, compound="left", text="Date of birth :")

        if self.date_status == True:
            print("date have been filled in")

    # get user email
    def get_email(self, email_entry, email_title, email_label):
        self.user_email = email_entry.get()
        self.email_status = False

        email_address = ['@email.com', '@gmail.com', '@yahoo.com']
        if any(self.user_email.endswith(domain) for domain in email_address):
            email_label.config(fg="#FFFFFF")
            email_title.config(image="", text="Email :")
            self.email_status = True
        else:
            email_label.config(fg="#FF0000")
            email_title.config(image=self.aset.red_dot, compound="left", text="Email :")
            email_title.image = self.aset.red_dot
            self.email_status = False


        if self.email_status == True:
            print("email have been filled in")

    # get user data
    def get_user_data(self, fullname_entry, date_button, gender_combobox, email_entry, password_entry, root):
        if self.name_and_password_status == True and self.date_status == True and self.gender_status == True and self.email_status == True:
            fullname_entry.delete(0, 'end')
            date_button.config(text="")
            gender_combobox.current(0)
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            fullname_entry.focus()

            self.user_data['Full name'].append(self.user_fullname)
            self.user_data['Date of birth'].append(self.user_birthdate)
            self.user_data['Gender'].append(self.user_gender)
            self.user_data['Email'].append(self.user_email)
            self.user_data['Password'].append(self.user_password)
            print(self.user_data)

            csv_file = "organizing_data/user_data.csv"
            with open(csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                # Write header
                writer.writerow(self.user_data.keys())
                # Write self.user_data
                rows = zip(*self.user_data.values())
                writer.writerows(rows)

            thanks_window = Toplevel(root)
            thanks_window.attributes('-topmost', bool(True))
            thanks_window.title("Thank you for sign up")
            thanks_window.geometry("320x145")
            thanks_window.resizable(False, False)
            thanks_window.configure(bg="#ffffff")

            thanks_label = Label(thanks_window,
                                text="Thank you\nfor sign up! :D",
                                bg="#ffffff", fg="#2E2E2E",
                                font=("roboto", 15, 'bold'))
            thanks_label.pack(pady=20)

            close_btn = Button(thanks_window,
                            text="Close",
                            command=lambda: thanks_window.destroy())
            close_btn.pack(pady=(20,0), fill='x')
        else:
            return None