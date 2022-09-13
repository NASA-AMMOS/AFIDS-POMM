from tkinter import Button, CENTER, W, NE, NW, N, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, OUTLINE
from components.title import Title
from components.param import Param


def Number(self, component, startY, parent, command, curVal):
    startY = Title(self, component, startY)

    H = 28

    if 'param' in component:
        Param(self, component['param'], startY + (H/2))

    defVal = ''
    if (curVal):
        defVal = str(curVal)

    numberValue = StringVar()
    numberValue.set(defVal)

    def setState(self, *args):
        parent.state.set_state(
            command, component['param'], cast(numberValue.get()))
    numberValue.trace('w', setState)

    def cast(val):
        if val == '':
            return val
        if 'options' in component and 'subtype' in component['options'] and component['options']['subtype'] == 'integer':
            return int(val)
        else:
            return float(val)

    def validate(action, index, value_if_allowed):
        if value_if_allowed:
            try:
                f = cast(value_if_allowed)
                if 'options' in component and 'min' in component['options'] and 'max' in component['options'] and 'step' in component['options']:
                    if f >= component['options']['min'] and f <= component['options']['max'] and ((f - component['options']['min']) % component['options']['step']) == 0:
                        return True
                    else:
                        return False
                return True
            except ValueError:
                return False
        else:
            return True

    vcmd = (self.register(validate), '%d', '%i', '%P')
    entry = ttk.Entry(self, bootstyle="secondary",
                      textvariable=numberValue, validate='key', validatecommand=vcmd)
    entry.place(y=startY, relx=0.2, relwidth=0.7)

    startY = startY + H

    return startY
