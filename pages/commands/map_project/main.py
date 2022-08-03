from tkinter import Frame, CENTER
import ttkbootstrap as ttk

def map_project():
    MapProject()

class MapProject(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="Map Projection", font=('Segoe UI', '16') )
        label.place(y=32, relx=.5, rely=0,anchor=CENTER)

        self.config = self.parent.config['MapProject']

        for (index, page) in enumerate(self.config['pages']):
            print(page)

        self.setPage(0)

    def setPage(self, page):
        print('mpDRAW', page)