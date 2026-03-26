from tkinter import *
from frame import Main_Frame

class Main_Element:
    def __init__(self, login_window):
        self.login_win = login_window
        self.frame = Main_Frame()

    # login title window
    def Title(self):
        title = Label(self.frame.frame_title,
                      text="Login",
                      font=("roboto", 25, "bold"),
                      fg="#2E2E2E",
                      bg="#ffffff")
        title.grid(row=0, column=0, pady=20)

    # title and input class
    class Entry:
        def __init__(self, config):
            self.frame = config.get("frame", None)
            self.title = config.get("title", "")
            self.title_row = config.get("title row", 0)
            self.title_col = config.get("title col", 0)
            self.entry_row = config.get("entry row", 0)
            self.entry_col = config.get("entry col", 0)
        def title_entry(self):
            title_e = Label(self.frame,
                       text=self.title,
                       bg="#ffffff",
                       fg="#2E2E2E")
            title_e.grid(row=self.title_row, column=self.title_col, sticky='w')

        def typebar_entry(self):
            typebar_e = Entry(self.frame,
                              bg="#eeeeee",
                              relief='flat',
                              bd=1,
                              width=30)
            typebar_e.grid(row=self.entry_row, column=self.entry_col, pady=(0,10))


    def username_entry(self):
        self.config = {"frame" : self.frame.frame_entry,
                       "title" : "Username :",
                       "title row" : 1,
                       "title col" : 0,
                       "entry row" : 2,
                       "entry col" : 0}
        self.username = self.Entry(self.config)
        self.username.title_entry()
        self.username.typebar_entry()

    def email_entry(self):
        self.config = {"frame" : self.frame.frame_entry,
                       "title" : "Email :",
                       "title row" : 3,
                       "title col" : 0,
                       "entry row" : 4,
                       "entry col" : 0}
        self.username = self.Entry(self.config)
        self.username.title_entry()
        self.username.typebar_entry()

    def password_entry(self):
        self.config = {"frame" : self.frame.frame_entry,
                       "title" : "Password :",
                       "title row" : 5,
                       "title col" : 0,
                       "entry row" : 6,
                       "entry col" : 0}
        self.username = self.Entry(self.config)
        self.username.title_entry()
        self.username.typebar_entry()