from tkinter import Button, CENTER, W, NE, NW, N, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, OUTLINE
from components.title import Title  

def Number(self, component, startY):
    startY = Title(self, component, startY)

    numberValue = StringVar()
    numberValue.set('')

    def validate(action, index, value_if_allowed):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return True

    vcmd = (self.register(validate), '%d', '%i', '%P')
    entry = ttk.Entry(self, bootstyle="secondary", textvariable=numberValue, validate='key', validatecommand=vcmd)
    entry.place(y=startY, relx=0.1, relwidth=0.8)

    startY = startY + 28

    return startY

