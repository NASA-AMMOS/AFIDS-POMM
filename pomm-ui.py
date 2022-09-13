from tkinter import Tk, PhotoImage, Frame
import ttkbootstrap as ttk
import json
# import ctypes
# from ctypes import alignment

from src.state import State

from src.pages.root.splash.main import Splash
from src.pages.root.planet.main import Planet
from src.pages.root.command.main import Command
from src.pages.commands.co_register.main import CoRegister
from src.pages.commands.map_project.main import MapProject
from src.pages.commands.mosaic.main import Mosaic
from src.pages.root.run.main import Run

# ctypes.windll.shcore.SetProcessDpiAwareness(True)

# This is the DPI of the computer you're making/testing the script on.
ORIGINAL_DPI = 96.09458128078816


def get_dpi():
    screen = Tk()
    current_dpi = screen.winfo_fpixels('1i')
    screen.destroy()
    return current_dpi


SCALE = get_dpi()/ORIGINAL_DPI
# Now every time you use a dimension in pixels, replace it with scaled(*pixel dimension*)


def scaled(original_width):
    return round(original_width * SCALE)


class App(Tk):
    def __init__(self):
        super().__init__()

        # Now this is the appropriate scale factor you were mentioning.
        self.SCALE = SCALE

        #ttk.utility.enable_high_dpi_awareness(root=self, scaling=SCALE)

        self.state = State()

        self.style = ttk.Style("flatly")
        self.style.configure('TButton', font=('helvetica', '11'))
        self.style.configure('Toolbutton', font=('helvetica', '11'))
        self.style.configure('primary.TButton', font=('helvetica', '9'))

        # Setting up Initial Things
        self.title("POMM")
        self.geometry(f'{scaled(800)}x{scaled(700)}')
        self.resizable(False, True)
        self.iconphoto(False, PhotoImage(file="src/assets/main-logo.png"))

        # Load config
        with open('src/configuration.json', 'r') as config:
            self.config = json.load(config)

        # Creating a container
        container = Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize Frames
        self.frames = {}
        self.Splash = Splash
        self.Planet = Planet
        self.Command = Command
        self.CoRegister = CoRegister
        self.MapProject = MapProject
        self.Mosaic = Mosaic

        self.pages = {
            'Splash': Splash,
            'Planet': Planet,
            'Command': Command,
            'CoRegister': CoRegister,
            'MapProject': MapProject,
            'Mosaic': Mosaic,
            'Run': Run
        }

        # Defining Frames and Packing it
        for p in self.pages:
            frame = self.pages[p](self, container)
            self.frames[p] = frame
            frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, y=0)

        self.show_frame('Splash')

    def show_frame(self, cont):
        frame = self.frames[cont]
        if (callable(getattr(frame, 'onRaise', None))):
            frame.onRaise()
        frame.tkraise()  # This line will put the frame on front


if __name__ == "__main__":
    app = App()
    app.mainloop()
