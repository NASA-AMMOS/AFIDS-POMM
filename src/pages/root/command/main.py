from tkinter import Frame, PhotoImage, Button, CENTER
import ttkbootstrap as ttk

from src.components.tophelp import TopHelp
from src.components.help import Help


def command():
    Command()


class Command(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="Choose an Operation",
                          font=('helvetica', '16', 'bold'))
        label.place(y=32, relx=.5, rely=0, anchor=CENTER)

        cardH = 128
        imageH = 96
        cardS = 16

        COMMANDS = [
            ('Mosaic', 'mosaic', 'Mosaic', 'Combines Several Map-Projected Orbital Images',
             'Put all your input Map-Projected images in one local directory.'),
            ('Co-Registration', 'coregister', 'CoRegister', 'Stack Two Map Orbital Images',
             ''),
            ('Map Project', 'mapproject', 'MapProject', 'Transform a raw PDS image to GIS/Map Format',
             'Copy a raw PDS image into your local directory.')
        ]

        self.helpIcons = {}
        self.buttonHelps = {}
        self.cards = {}

        hlbg = "#ffffff"
        hlbgA = "#3498db"
        hlth = 2
        hlthA = 2

        for index, (text, val, page, desc, req) in enumerate(COMMANDS):
            card = Frame(self, highlightbackground=hlbg,
                         highlightthickness=hlth)
            card.place(y=132 + (index * cardH) + (index * cardS),
                       relx=.5, relwidth=0.9, height=cardH, anchor=CENTER)

            # Event Functions
            def enter_card(index):
                return lambda e: self.cards[index].config(highlightbackground=hlbgA, highlightthickness=hlthA)

            def leave_card(index):
                return lambda e: self.cards[index].config(highlightbackground=hlbg, highlightthickness=hlth)

            def select(page):
                return lambda e: self.setCommand(page)

            def openHelp(index):
                return lambda: Help(COMMANDS[index][1])

            img = PhotoImage(file="src/assets/" + val + ".png")
            button = Button(
                card,
                image=img,
                command=select(page)
            )
            button.img = img
            button.configure(background='#FFFFFF')
            button.place(y=16, x=16, width=imageH, height=imageH)

            label = ttk.Label(
                card,
                text=text,
                font=('helvetica', '16')
            )
            label.place(y=20, x=128)
            label2 = ttk.Label(
                card,
                text=desc,
                font=('helvetica', '12')
            )
            label2.place(y=50, x=128)
            label3 = ttk.Label(
                card,
                text=req,
                font=('helvetica', '10')
            )
            label3.place(y=74, x=128)

            self.cards[index] = card

            # Events
            self.cards[index].bind("<Enter>", enter_card(index))
            self.cards[index].bind("<Leave>", leave_card(index))
            self.cards[index].bind("<Button-1>", select(page))
            label.bind("<Button-1>", select(page))
            label2.bind("<Button-1>", select(page))
            label3.bind("<Button-1>", select(page))

            # Help
            headH = 30

            self.helpIcons[index] = PhotoImage(file="src/assets/help.png")
            self.buttonHelps[index] = Button(
                card,
                image=self.helpIcons[index],
                command=openHelp(index),
                width=headH,
                height=headH
            )
            self.buttonHelps[index].configure(background='#FFFFFF',
                                              activebackground='#FFFFFF')
            self.buttonHelps[index].place(width=headH, height=headH,
                                          relx=0.9, rely=0.5, anchor=CENTER)

        TopHelp(self, "command")

    def setCommand(self, command):
        self.parent.state.set_state('core', 'command', command)
        self.parent.show_frame(command)
