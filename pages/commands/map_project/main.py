from tkinter import Frame, Button, CENTER, BOTTOM, E, SE, SW
from components.ComponentRenderer import ComponentRenderer
import ttkbootstrap as ttk
from ttkbootstrap.constants import INFO, OUTLINE

from components.tophelp import TopHelp


def map_project():
    MapProject()


class MapProject(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="Map Projection", font=('Segoe UI', '16', 'bold'))
        label.place(y=32, relx=.5, rely=0, anchor=CENTER)

        self.config = self.parent.config['MapProject']

        self.innerFrame = Frame(self)
        self.innerFrame.place(
            relx=0, rely=0, relwidth=1.0, relheight=1.0, y=48)

        self.page = 0
        self.setPage(self.page)

        TopHelp(self, "mapproject-about")

        # Continue
        buttonContinue = ttk.Button(
            self,
            text="Continue",
            command=lambda: self.forward(),
            bootstyle=(INFO)
        )
        buttonContinue.place(rely=1.0, relx=1.0, relwidth=0.8, anchor=SE)

        # Back
        buttonBack = ttk.Button(
            self,
            text="Back",
            command=lambda: self.backward()
        )
        buttonBack.place(rely=1.0, relx=0.0, relwidth=0.2, anchor=SW)

    def forward(self):
        if (self.page + 1 < len(self.config['pages'])):
            self.setPage(self.page + 1)
        else:
            self.parent.show_frame("Run")

    def backward(self):
        if (self.page - 1 >= 0):
            self.setPage(self.page - 1)
        else:
            self.parent.show_frame("Command")

    def setPage(self, page):
        self.page = page
        ComponentRenderer(self, self.parent, self.innerFrame,
                          self.config['pages'][page]['components'], 'MapProject')
