from tkinter import StringVar
import ttkbootstrap as ttk

from src.components.title import Title
from src.components.param import Param


def String(self, component, startY, parent, command, curVal):
    startY = Title(self, component, startY)

    H = 28

    if 'param' in component:
        Param(self, component['param'], startY + (H/2))

    defVal = ''
    if (curVal):
        defVal = str(curVal)

    stringValue = StringVar()
    stringValue.set(defVal)

    def setState(self, *args):
        parent.state.set_state(
            command, component['param'], stringValue.get())
    stringValue.trace('w', setState)

    def validate(action, index, value_if_allowed):
        if value_if_allowed:
            if ('options' in component):
                if ('maxLength' in component['options'] and len(value_if_allowed) > component['options']['maxLength']):
                    return False
                if ('forbid' in component['options'] and any(ele in value_if_allowed for ele in component['options']['forbid'])):
                    return False
                return True
            else:
                return True
        else:
            return True

    vcmd = (self.register(validate), '%d', '%i', '%P')
    entry = ttk.Entry(self, bootstyle="secondary",
                      textvariable=stringValue, validate='key', validatecommand=vcmd)
    entry.place(y=startY, relx=0.2, relwidth=0.7)

    startY = startY + H

    return startY
