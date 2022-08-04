from tkinter import Button, CENTER, W, NE, NW, N, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from components.title import Title  

def RadioList(self, component, startY):
    startY = Title(self, component, startY)

    sFrameH = 100

    sFrame = ScrolledFrame(self, height=sFrameH)
    sFrame.vscroll.configure(bootstyle='secondary')
    sFrame.container.configure(bootstyle='secondary')
    sFrame.place(y=startY, relx=0.5, relwidth=0.8, anchor=N)

    nSep = ttk.Separator(self)
    nSep.place(y=startY - 1, relx=0.5, relwidth=0.8, anchor=N)
    wSep = ttk.Separator(self, orient='vertical')
    wSep.place(y=startY - 1, relx=0.1, height=sFrameH, anchor=NW)
    sSep = ttk.Separator(self)
    sSep.place(y=startY + sFrameH + 1, relx=0.5, relwidth=0.8, anchor=N)

    radioValue = StringVar()
    radioValue.set('')

    for (index, item) in enumerate(component['options']['items']):
        name = item['name']
        value = item['value']
        rb = ttk.Radiobutton(sFrame, text=name, variable=radioValue, value=value, bootstyle="success")
        #rb.place(y=(index * 30), x=20, relx=0, rely=0)
        rb.grid(row=index, column=0, padx=20, ipady=4, sticky=NW)

    startY = startY + sFrameH

    return startY

        