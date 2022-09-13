from tkinter import Frame, Label, PhotoImage, CENTER, SW
import ttkbootstrap as ttk
from ttkbootstrap.constants import INFO, OUTLINE

from src.components.tophelp import TopHelp


def splash():
    Splash()


class Splash(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.groupImg = PhotoImage(file="src/assets/group-logo.png")
        groupLogo = Label(self, image=self.groupImg)
        groupLogo.place(relx=0.02, rely=0.98, width=100,
                        height=40, anchor=SW)

        label = ttk.Label(self, text="POMM", font=('lucida', '36'))
        label.place(height=50, relx=.5, rely=.25, anchor=CENTER)
        label = ttk.Label(
            self, text="Planetary Orbital Mosaicking and Mapping", font=('helvetica', '16'))
        label.place(y=56, relx=.5, rely=.25, anchor=CENTER)

        button = ttk.Button(
            self,
            text="Begin",
            command=lambda: parent.show_frame('Planet'),
            bootstyle=(INFO, OUTLINE)
        )
        button.place(y=118, relx=.5, rely=.25,
                     width=100, height=40, anchor=CENTER)

        TopHelp(self, 'pomm')
