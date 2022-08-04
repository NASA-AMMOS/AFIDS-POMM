import os
from tkinter import filedialog, Button, CENTER, W, NE, NW, N, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, OUTLINE
from components.title import Title  

def FilePath(self, component, startY):
    startY = Title(self, component, startY)

    pathValue = StringVar()
    pathValue.set('')
    entry = ttk.Entry(self, bootstyle="secondary", textvariable=pathValue)
    entry.place(y=startY, relx=0.1, relwidth=0.6)

    def browseDirectory():
        return filedialog.askdirectory(
            initialdir=os.getcwd(),
            title="POMM - " + component['title'] +" - Select A Directory"
        )

    browseButton = ttk.Button(
        self, 
        text="Browse", 
        command=lambda: pathValue.set(browseDirectory()),
        bootstyle=(PRIMARY)
    )
    browseButton.place(y=startY, relx=0.7, relwidth=0.2)

    startY = startY + 28

    return startY

