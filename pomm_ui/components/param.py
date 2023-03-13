from tkinter import E
import ttkbootstrap as ttk


def Param(self, param, startY):
    label = ttk.Label(self, text=param + ' =', font=('Consolas', '10'))
    label.configure(foreground='#666666')
    label.place(y=startY, relx=0.185, anchor=E)
