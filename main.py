import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog as tkfd


class ArnoldApp(tk.Tk):

    # This is the main backend class

    def __init__(self):

        # Call the parents constructor
        tk.Tk.__init__(self)

        # Set the window title
        tk.Tk.wm_title(self, "Arnold")

        # Set the window size
        self.geometry('{}x{}'.format(800,600))
