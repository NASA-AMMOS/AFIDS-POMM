from tkinter import Button, CENTER, W, NE, NW, N, StringVar, Text, Scrollbar, RIGHT
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
import re

from components.title import Title
from components.param import Param


def MultiText(self, component, startY, parent, command, curParams):
    startY = Title(self, component, startY)

    fontsize = 10
    viewrows = 8
    sFrameH = (fontsize + 9) * viewrows

    if 'param' in component:
        Param(self, component['param'], startY + (sFrameH/2))

    v = Scrollbar(self, orient='vertical')

    text = Text(self, height=viewrows, wrap="none",
                font=('helvetica', fontsize),
                yscrollcommand=v.set)

    text.place(y=startY, relx=0.2, relwidth=0.7, anchor=NW)
    v.config(command=text.yview)
    v.place(in_=text, relx=1.0, relheight=1.0, bordermode="outside")

    idx = 1
    for (index, item) in enumerate(component['options']['items']):
        param = item['param']
        value = item['value']
        if (curParams and param in curParams):
            value = str(curParams[param])
        if ('comment' in item):
            text.insert('end', '# ' + item['comment'] + ':\n')
            text.tag_add("comment", str(idx) + ".0", str(idx) + ".end")
            idx = idx + 1
        text.insert('end', str(param) + '=' + str(value) + '\n')
        idx = idx + 1

    text.tag_config("comment", foreground="#888888")

    def setState(self, *args):
        textBody = text.get("1.0", "end").splitlines()
        for param in textBody:
            if (len(param) > 0 and param[:1] != '#' and re.search('=', param)):
                pv = param.split('=')
                parent.state.set_state(command, pv[0], pv[1])
    text.tag_add("all", "1.0", "end")
    text.tag_bind("all", "<KeyRelease>", setState)

    # Trigger default state
    setState(self)

    startY = startY + sFrameH

    return startY
