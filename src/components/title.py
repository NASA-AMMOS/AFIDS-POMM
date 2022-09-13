from tkinter import Button, NE
import ttkbootstrap as ttk

from src.components.help import Help


def Title(self, component, startY):
    headH = 30

    relx = 0.2
    fontsize = '12'
    if 'indent' in component and component['indent'] == True:
        relx = 0.25
        fontsize = '10'

    label = ttk.Label(
        self, text=component['title'], font=('helvetica', fontsize))
    label.place(y=startY, relx=relx)

    def openHelp():
        if ('help' in component):
            Help(component['help'])
        else:
            Help('none')

    buttonHelp = Button(
        self,
        image=self.helpIcon,
        command=lambda: openHelp(),
        width=headH,
        height=headH
    )
    buttonHelp.configure(background='#FFFFFF', activebackground='#FFFFFF')
    buttonHelp.place(width=20, height=headH, y=startY, relx=0.9, anchor=NE)

    startY = startY + 32

    return startY
