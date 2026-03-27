from tkinter import *
from frame import Main_Frame
from function import Main_Function
from aset import Aset

class Main_Element:
    def __init__(self, login_window):
        self.login_win = login_window
        self.frame = Main_Frame()
        self.main_func = Main_Function()
        self.aset = Aset()

    # login title window
    def Title(self):
        title = Label(self.frame.frame_title,
                      text="Sign Up",
                      font=("roboto", 25, "bold"),
                      fg="#2E2E2E",
                      bg="#ffffff")
        title.grid(row=0, column=0, pady=(30,20))

    # title entry + input entry class
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

    # fullname entry
    def fullname_entry(self):
        self.config = {"frame" : self.frame.frame_entry,
                       "title" : "Full name :",
                       "title row" : 1,
                       "title col" : 0,
                       "entry row" : 2,
                       "entry col" : 0}
        self.fullname = self.Entry(self.config)
        self.fullname.title_entry()
        self.fullname.typebar_entry()

    # date of birth entry
    def date_entry(self, root):
        # date entry title
        date_title = Label(self.frame.frame_entry,
                           text="Date of birth",
                           bg="#ffffff",
                           fg="#2E2E2E")
        date_title.grid(row=3, column=0, sticky='w')
        # open calendar button
        date_btn = Button(self.frame.frame_entry,
                          text="Open Calendar",
                          anchor='w',
                          pady=1,
                          padx=1,
                          width=30,
                          bd=0,
                          bg="#eeeeee",
                          fg="#2E2E2E",
                          command=lambda: self.main_func.open_calendar(root, date_btn))
        date_btn.grid(row=4, column=0, pady=(0,10))

    # email entry
    def email_entry(self):
        self.config = {"frame" : self.frame.frame_entry,
                       "title" : "Email :",
                       "title row" : 5,
                       "title col" : 0,
                       "entry row" : 6,
                       "entry col" : 0}
        self.email = self.Entry(self.config)
        self.email.title_entry()
        self.email.typebar_entry()

    # password entry
    def password_entry(self):
        self.config = {"frame" : self.frame.frame_entry,
                       "title" : "Password :",
                       "title row" : 7,
                       "title col" : 0,
                       "entry row" : 8,
                       "entry col" : 0}
        self.password = self.Entry(self.config)
        self.password.title_entry()
        self.password.typebar_entry()

    # sign up button
    def sign_up_button(self):
        signup_btn = Button(self.frame.frame_entry,
                            text="Sign Up",
                            font=("sistem ui", 10, "bold"),
                            bg="#5b7038",
                            fg="#ffffff",
                            padx=1,
                            width=30)
        signup_btn.grid(row=9, column=0, pady=(50,0))

    # image label
    def image_label(self):
        img = Label(self.frame.right_frame,
                    image=self.aset.label_img)
        img.pack()