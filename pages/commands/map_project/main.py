from tkinter import Frame, Button, CENTER, BOTTOM, E
from components.ComponentRenderer import ComponentRenderer
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS, OUTLINE


def map_project():
    MapProject()


class MapProject(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="Map Projection", font=('Segoe UI', '16'))
        label.place(y=32, relx=.5, rely=0, anchor=CENTER)

        self.config = self.parent.config['MapProject']

        self.innerFrame = Frame(self)
        self.innerFrame.place(
            relx=0, rely=0, relwidth=1.0, relheight=1.0, y=48)

        self.page = 0
        self.setPage(self.page)

        # Continue
        button = ttk.Button(
            self,
            text="Continue",
            command=lambda: self.setPage(self.page + 1),
            bootstyle=(SUCCESS)
        )

        button.pack(side=BOTTOM, padx=12, pady=42, anchor=E)

    def setPage(self, page):
        self.page = page
        ComponentRenderer(self, self.parent, self.innerFrame,
                          self.config['pages'][page]['components'], 'MapProject')
