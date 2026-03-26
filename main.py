from tkinter import *
from element import Main_Element

class Login_Window:
    def __init__(self):
        self.login_win = Tk()
        self.win_setup()

        # main element
        self.main_elm = Main_Element(self.login_win)
        self.main_elm.Title()
        self.main_elm.username_entry()
        self.main_elm.email_entry()
        self.main_elm.password_entry()

    def win_setup(self):
        self.login_win.geometry("400x500")
        self.login_win.title("Login Window")
        self.login_win.configure(bg="#FFFFFF")
        
    def run(self):
        self.login_win.mainloop()

if __name__ == "__main__":
    window = Login_Window()
    window.run()