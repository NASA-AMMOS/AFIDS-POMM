from tkinter import Frame

def co_register():
    CoRegister()

class CoRegister(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent