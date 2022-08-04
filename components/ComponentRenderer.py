from tkinter import PhotoImage
import ttkbootstrap as ttk

from components.radiolist import RadioList
from components.title import Title
from components.filepath import FilePath
from components.filename import FileName
from components.number import Number

def ComponentRenderer(self, components):
    self.helpIcon = PhotoImage(file="assets/help.png")
    
    # To keep track of the starting y position of each component
    y = 48
    componentSpacing = 16

    for (index, component) in enumerate(components):
        t = component['type']
        y = y + componentSpacing
        if(t == 'radiolist'):
            y = RadioList(self, component, y)
        elif(t == 'title'):
            y = Title(self, component, y)
        elif(t == 'filepath'):
            y = FilePath(self, component, y)
        elif(t == 'filename'):
            y = FileName(self, component, y)
        elif(t == 'number'):
            y = Number(self, component, y)
