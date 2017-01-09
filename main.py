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

        frame = MainPage(self.container, self)
        self.frames[MainPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        # set the starting page
        self.show_frame(MainPage)

    def show_frame(self, cont):

        # A simple function to switch pages

        frame = self.frames[cont]
        frame.set_menu_bar()
        frame.tkraise()


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
        self.text_area.config(background="#444", foreground="white")
        self.text_area.pack(side="top", fill="both", expand=True)

        # Create the menu bar and add it to the parent window
        self.menu_bar = tk.Menu(self.controller)
        self.set_menu_bar = lambda: self.controller.config(menu=self.menu_bar)

app = ArnoldApp()
app.mainloop()
