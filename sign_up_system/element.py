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
            self.title_e = Label(self.frame,
                       text=self.title,
                       bg="#ffffff",
                       fg="#2E2E2E")
            self.title_e.grid(row=self.title_row, column=self.title_col, sticky='w')

        def typebar_entry(self):
            self.typebar_e = Entry(self.frame,
                              bg="#eeeeee",
                              relief='flat',
                              bd=1,
                              width=30)
            self.typebar_e.grid(row=self.entry_row, column=self.entry_col, pady=(0,0))

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
        self.date_title = Label(self.frame.frame_entry,
                           text="Date of birth",
                           bg="#ffffff",
                           fg="#2E2E2E")
        self.date_title.grid(row=3, column=0, sticky='w', pady=(20,0))
        # open calendar button
        self.date_btn = Button(self.frame.frame_entry,
                          text="",
                          anchor='w',
                          pady=1,
                          padx=1,
                          bd=0,
                          width=30,
                          bg="#eeeeee",
                          fg="#2E2E2E",
                          command=lambda: self.main_func.open_calendar(root, self.date_btn))
        self.date_btn.grid(row=4, column=0, pady=(0,20))

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

    def email_warn(self):
        self.email_label = Label(self.frame.frame_entry,
                          text="email not valid!",
                          bg="#ffffff",
                          fg="#FFFFFF",
                          font=("system ui", 9),
                          pady=0)
        self.email_label.grid(row=7, column=0)

    # password entry
    def password_entry(self):
        self.config = {"frame" : self.frame.frame_entry,
                       "title" : "Password :",
                       "title row" : 8,
                       "title col" : 0,
                       "entry row" : 9,
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
                            width=30,
                            command=lambda: [(self.main_func.get_name_pass(self.fullname.typebar_e, self.fullname.title_e,
                                                                         self.password.typebar_e, self.password.title_e)),
                                            (self.main_func.get_email(self.email.typebar_e, self.email.title_e, self.email_label)),
                                            (self.main_func.get_birth_date(self.date_title)),
                                            (self.main_func.get_user_data(self.fullname.typebar_e, self.date_btn,
                                                                          self.email.typebar_e, self.password.typebar_e))])
        signup_btn.grid(row=10, column=0, pady=(50,0))

    # image label
    def image_label(self):
        img = Label(self.frame.right_frame,
                    image=self.aset.label_img)
        img.pack()

    