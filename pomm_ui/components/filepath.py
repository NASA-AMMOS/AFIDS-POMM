import os
from tkinter import filedialog, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY

from pomm_ui.components.title import Title
from pomm_ui.components.param import Param


def FilePath(self, component, startY, parent, command, curVal):
    startY = Title(self, component, startY)

    H = 28

    if 'param' in component:
        Param(self, component['param'], startY + (H/2))

    defVal = ''
    if (curVal):
        defVal = str(curVal)

    pathValue = StringVar()
    pathValue.set(defVal)

    def setState(self, *args):
        parent.state.set_state(command, component['param'], pathValue.get())
    pathValue.trace('w', setState)

    entry = ttk.Entry(self, bootstyle="secondary", textvariable=pathValue)
    entry.place(y=startY, relx=0.2, relwidth=0.6)

    def browseDirectory():
        return filedialog.askdirectory(
            initialdir=os.getcwd(),
            title="POMM - " + component['title'] + " - Select A Directory"
        )

    browseButton = ttk.Button(
        self,
        text="Browse",
        command=lambda: pathValue.set(browseDirectory()),
        bootstyle=(PRIMARY)
    )
    browseButton.place(y=startY, relx=0.8, relwidth=0.1)

    startY = startY + H

    return startY
