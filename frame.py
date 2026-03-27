import tkinter as tk

class Main_Frame:
    def __init__(self):
    # left frame
        self.left_frame = tk.Frame(bg="#ffffff")
        self.left_frame.pack(side="left", anchor='n', padx=70)

        # title frame
        self.frame_title = tk.Frame(self.left_frame, bg="#ffffff")
        self.frame_title.pack()

        # entry frame
        self.frame_entry = tk.Frame(self.left_frame, bg="#ffffff")
        self.frame_entry.pack()

    # right frame
        self.right_frame = tk.Frame(bg="#ffffff")
        self.right_frame.pack(side="right")