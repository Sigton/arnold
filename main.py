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
        self.geometry('{}x{}'.format(800, 600))

        # Create the container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # And configure the grid
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Create a dictionary of frames and add all pages to it
        self.frames = {}

    def show_frame(self, cont):

        # A simple function to switch pages

        frame = self.frames[cont]
        frame.tkraise()
        frame.set_menubar()


class MainPage(tk.Frame):

    # This is all content on the main page

    def __init__(self, parent, controller):

        # Call the parents constructor
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        # Add the content

        # Fill the whole window with a text box to be typed into
        self.text_area = ScrolledText(self)
        self.text_area.pack(side="top", fill="both", expand=True)
