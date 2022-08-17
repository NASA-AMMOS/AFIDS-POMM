from tkinter import PhotoImage
import ttkbootstrap as ttk

from components.radiolist import RadioList
from components.title import Title
from components.filepath import FilePath
from components.filename import FileName
from components.filepathname import FilePathName
from components.number import Number
from components.boolean import Boolean
from components.string import String
from components.multitext import MultiText


def ComponentRenderer(self, parent, frame, components, command):
    # destroy all widgets from frame
    for widget in frame.winfo_children():
        widget.destroy()

    frame.helpIcon = PhotoImage(file="assets/help.png")

    # To keep track of the starting y position of each component
    y = 0
    componentSpacing = 16

    for (index, component) in enumerate(components):
        t = component['type']
        y = y + componentSpacing
        if (t == 'radiolist'):
            y = RadioList(frame, component, y, parent, command)
        elif (t == 'title'):
            y = Title(frame, component, y)
        elif (t == 'filepath'):
            y = FilePath(frame, component, y, parent, command)
        elif (t == 'filename'):
            y = FileName(frame, component, y, parent, command)
        elif (t == 'filepathname'):
            y = FilePathName(frame, component, y, parent, command)
        elif (t == 'number'):
            y = Number(frame, component, y, parent, command)
        elif (t == 'boolean'):
            y = Boolean(frame, component, y, parent, command)
        elif (t == 'string'):
            y = String(frame, component, y, parent, command)
        elif (t == 'multitext'):
            y = MultiText(frame, component, y, parent, command)
