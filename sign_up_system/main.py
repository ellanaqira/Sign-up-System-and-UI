from tkinter import *
from element import Main_Element

class Login_Window:
    def __init__(self):
        self.login_win = Tk()
        self.win_setup()

        # main element
        self.main_elm = Main_Element(self.login_win)
        self.main_elm.Title()
        self.main_elm.fullname_entry()
        self.main_elm.gender_combobox()
        self.main_elm.date_entry(self.login_win)
        self.main_elm.email_entry()
        self.main_elm.email_warn()
        self.main_elm.password_entry()
        self.main_elm.sign_up_button()
        self.main_elm.image_label()

    def win_setup(self):
        self.login_win.geometry("785x540")
        self.login_win.resizable(False, False)
        self.login_win.title("Login Window")
        self.login_win.configure(bg="#ffffff")
        
    def run(self):
        self.login_win.mainloop()

if __name__ == "__main__":
    window = Login_Window()
    window.run()