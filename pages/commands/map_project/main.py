from tkinter import Frame

def map_project():
    MapProject()

class MapProject(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent