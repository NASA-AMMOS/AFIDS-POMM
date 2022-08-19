from tkinter import Button, CENTER, W, NE, NW, N, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from components.title import Title
from components.param import Param


def RadioList(self, component, startY, parent, command):
    startY = Title(self, component, startY)

    sFrameH = min(len(component['options']['items']) * 24, 150)

    if 'param' in component:
        Param(self, component['param'], startY + (sFrameH/2))

    sFrame = ScrolledFrame(self, height=sFrameH)
    sFrame.vscroll.configure(bootstyle='secondary')
    sFrame.container.configure(bootstyle='secondary')
    sFrame.place(y=startY, relx=0.2, relwidth=0.7, anchor=NW)

    nSep = ttk.Separator(self)
    nSep.place(y=startY - 1, relx=0.2, relwidth=0.7, anchor=NW)
    wSep = ttk.Separator(self, orient='vertical')
    wSep.place(y=startY - 1, relx=0.2, height=sFrameH, anchor=NW)
    sSep = ttk.Separator(self)
    sSep.place(y=startY + sFrameH + 1, relx=0.2, relwidth=0.7, anchor=NW)

    radioValue = StringVar()
    radioValue.set('')

    for (index, item) in enumerate(component['options']['items']):
        name = item['name']
        value = item['value']
        rb = ttk.Radiobutton(
            sFrame, text=name,
            variable=radioValue,
            value=value,
            bootstyle="INFO",
            command=lambda: parent.state.set_state(
                command, component['param'], radioValue.get())
        )
        #rb.place(y=(index * 30), x=20, relx=0, rely=0)
        rb.grid(row=index, column=0, padx=8, ipady=4, sticky=NW)

    startY = startY + sFrameH

    return startY
