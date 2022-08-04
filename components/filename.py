import os
from tkinter import filedialog, Button, CENTER, W, NE, NW, N, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, OUTLINE
from components.title import Title  

def FileName(self, component, startY):
    startY = Title(self, component, startY)

    nameValue = StringVar()
    nameValue.set('')
    entry = ttk.Entry(self, bootstyle="secondary", textvariable=nameValue)
    entry.place(y=startY, relx=0.1, relwidth=0.6)

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
            title="POMM - " + component['title'] +" - Select A File",
            filetypes=filetypes
        )

        return os.path.basename(filename).split('/')[-1]

    browseButton = ttk.Button(
        self, 
        text="Browse", 
        command=lambda: nameValue.set(browseFile()),
        bootstyle=(PRIMARY)
    )
    browseButton.place(y=startY, relx=0.7, relwidth=0.2)

    startY = startY + 28

    return startY

