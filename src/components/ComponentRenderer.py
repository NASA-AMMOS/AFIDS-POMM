from tkinter import PhotoImage

from src.components.radiolist import RadioList
from src.components.title import Title
from src.components.filepath import FilePath
from src.components.filename import FileName
from src.components.filepathname import FilePathName
from src.components.number import Number
from src.components.boolean import Boolean
from src.components.string import String
from src.components.multitext import MultiText


def ComponentRenderer(self, parent, frame, components, command):
    state = parent.state.get_state()
    planet = state['core']['planet']

    params = None
    if (command):
        params = state[command]

    # destroy all widgets from frame
    for widget in frame.winfo_children():
        widget.destroy()

    frame.helpIcon = PhotoImage(file="src/assets/help.png")

    # To keep track of the starting y position of each component
    y = 0
    componentSpacing = 16

    for (index, component) in enumerate(components):
        t = component['type']
        p = None
        if ('param' in component):
            p = component['param']
        curVal = None
        if (p and params and p in params):
            curVal = params[p]

        y = y + componentSpacing
        if (t == 'radiolist'):
            y = RadioList(frame, component, y, parent, command, curVal)
        elif (t == 'title'):
            y = Title(frame, component, y)
        elif (t == 'filepath'):
            y = FilePath(frame, component, y, parent, command, curVal)
        elif (t == 'filename'):
            y = FileName(frame, component, y, parent, command, curVal)
        elif (t == 'filepathname'):
            y = FilePathName(frame, component, y, parent, command, curVal)
        elif (t == 'number'):
            y = Number(frame, component, y, parent, command, curVal)
        elif (t == 'boolean'):
            y = Boolean(frame, component, y, parent, command, curVal)
        elif (t == 'string'):
            y = String(frame, component, y, parent, command, curVal)
        elif (t == 'multitext'):
            y = MultiText(frame, component, y, parent, command, params)
