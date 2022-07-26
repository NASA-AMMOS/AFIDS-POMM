from tkinter import Frame

def mosaic():
    Mosaic()

class Mosaic(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent