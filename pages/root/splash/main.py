from tkinter import Frame, Label, CENTER
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS, OUTLINE

def splash():
    Splash()

class Splash(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="POMM", font=('Berlin Sans FB', '32') )
        label.place(height=42, relx=.5, rely=.30,anchor=CENTER)
        label = ttk.Label(self, text="Planetary Orbital Mosaicking and Mapping", font=('Segoe UI', '14') )
        label.place(y=50, relx=.5, rely=.30,anchor=CENTER)

        button = ttk.Button(
            self, 
            text="Begin", 
            command=lambda: parent.show_frame('Planet'),
            bootstyle=(SUCCESS, OUTLINE)
        )
        button.place(y=120, relx=.5, rely=.30,anchor=CENTER)