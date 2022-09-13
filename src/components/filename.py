import os
from tkinter import filedialog, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY

from src.components.title import Title
from src.components.param import Param


def FileName(self, component, startY, parent, command, curVal):
    startY = Title(self, component, startY)

    H = 28

    if 'param' in component:
        Param(self, component['param'], startY + (H/2))

    defVal = ''
    if (curVal):
        defVal = str(curVal)

    nameValue = StringVar()
    nameValue.set(defVal)

    def setState(self, *args):
        parent.state.set_state(command, component['param'], nameValue.get())
    nameValue.trace('w', setState)

    entry = ttk.Entry(
        self,
        bootstyle="secondary",
        textvariable=nameValue
    )
    entry.place(y=startY, relx=0.2, relwidth=0.6)

    def browseFile():
        filetypes = ()

        try:
            for (index, ext) in enumerate(component['options']['extensions']):
                filetypes += (ext['name'], ext['value']),
        except:
            pass

        filetypes += ("All files", "*.*"),

        filename = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="POMM - " + component['title'] + " - Select A File",
            filetypes=filetypes
        )

        return os.path.basename(filename).split('/')[-1]

    browseButton = ttk.Button(
        self,
        text="Browse",
        command=lambda: nameValue.set(browseFile()),
        bootstyle=(PRIMARY)
    )
    browseButton.place(y=startY, relx=0.8, relwidth=0.1)

    startY = startY + H

    return startY
