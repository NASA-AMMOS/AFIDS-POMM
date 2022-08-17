from tkinter import Button, CENTER, W, NE, NW, N, StringVar, Text
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
import re

from components.title import Title
from components.param import Param


def MultiText(self, component, startY, parent, command):
    startY = Title(self, component, startY)

    sFrameH = min(len(component['options']['items']) * 24, 250)

    if 'param' in component:
        Param(self, component['param'], startY + (sFrameH/2))

    text = Text(self, height=8, wrap="none")
    text.place(y=startY, relx=0.2, relwidth=0.7, anchor=NW)

    idx = 1
    for (index, item) in enumerate(component['options']['items']):
        param = item['param']
        value = item['value']
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
