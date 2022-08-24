from tkinter import Button, CENTER, W, NE, NW, N, IntVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, OUTLINE
from components.title import Title
from components.param import Param


def Boolean(self, component, startY, parent, command, curVal):
    startY = Title(self, component, startY)

    H = 28

    if 'param' in component:
        Param(self, component['param'], startY + (H/2))

    default = 0
    trueValue = 1
    falseValue = 0
    trueText = 'Yes (1)'
    falseText = 'No (0)'
    if ('options' in component):
        if ('default' in component['options'] and component['options']['default'] == True):
            default = 1
        if ('trueText' in component['options']):
            trueText = component['options']['trueText']
        if ('falseText' in component['options']):
            falseText = component['options']['falseText']
        if ('trueValue' in component['options']):
            trueValue = component['options']['trueValue']
        if ('falseValue' in component['options']):
            falseValue = component['options']['falseValue']

    if (curVal is not None):
        default = int(curVal)

    boolValue = IntVar()
    boolValue.set(default)

    def setState(self, *args):
        parent.state.set_state(command, component['param'], boolValue.get())
    boolValue.trace('w', setState)

    # trigger default state
    setState(self)

    t = ttk.Radiobutton(self, text=trueText,
                        variable=boolValue, value=trueValue, bootstyle="INFO")
    t.place(y=startY + 8, relx=0.2, relwidth=0.2)
    f = ttk.Radiobutton(self, text=falseText,
                        variable=boolValue, value=falseValue, bootstyle="secondary")
    f.place(y=startY + 8, relx=0.4, relwidth=0.2)

    startY = startY + H

    return startY
