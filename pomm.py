from ctypes import alignment
from tkinter import Tk, PhotoImage, Frame, Button, CENTER
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS, OUTLINE

from pages.root.splash.main import Splash
from pages.root.planet.main import Planet
from pages.root.command.main import Command
from pages.commands.co_register.main import CoRegister
from pages.commands.map_project.main import MapProject
from pages.commands.mosaic.main import Mosaic

headH = 30

class App(Tk):
    def __init__(self):
        super().__init__()

        style = ttk.Style("darkly")
        
        ## Setting up Initial Things
        self.title("POMM")
        self.geometry("768x624")
        self.resizable(True, True)
        self.iconphoto(False, PhotoImage(file="assets/pomm_logo.png"))

        ## Creating a container
        container = Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        headerBar = HeaderBar(self)
        headerBar.place(relx=0, rely=0, relwidth=1.0, height=headH)  


        ## Initialize Frames
        self.frames = {}
        self.Splash = Splash
        self.Planet = Planet
        self.Command = Command
        self.CoRegister = CoRegister
        self.MapProject = MapProject
        self.Mosaic = Mosaic

        self.pages = {'Splash': Splash, 'Planet': Planet, 'Command': Command, 'CoRegister': CoRegister, 'MapProject': MapProject, 'Mosaic': Mosaic}

        ## Defining Frames and Packing it
        for p in self.pages:
            frame = self.pages[p](self, container)
            self.frames[p] = frame
            frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, y=headH)    
           
        self.show_frame('Splash')

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()                         ## This line will put the frame on front
 
class HeaderBar(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.bg = '#1a1a1a'
        self.configure(background=self.bg)

        # Back Button
        iconLeft = PhotoImage(file="assets/arrow_left.png")
        buttonBack = Button(
            self, 
            image=iconLeft,
            command=lambda: parent.show_frame('Planet'),
            width=headH,
            height=headH
        )
        buttonBack.configure(background=self.bg)
        buttonBack.img = iconLeft
        buttonBack.place(width=headH, height=headH, x=0, y=0)

        # Forward Button
        iconRight = PhotoImage(file="assets/arrow_right.png")
        buttonForward = Button(
            self, 
            image=iconRight,
            command=lambda: parent.show_frame('Splash'),
            width=headH,
            height=headH
        )
        buttonForward.configure(background=self.bg)
        buttonForward.img = iconRight
        buttonForward.place(width=headH, height=headH, x=headH, y=0)

if __name__ == "__main__":
    app = App()
    app.mainloop()