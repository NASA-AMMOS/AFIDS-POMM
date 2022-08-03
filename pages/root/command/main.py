from tkinter import Frame, Label, W, E, BOTTOM, PhotoImage, Button, CENTER, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS, OUTLINE

def command():
    Command()

class Command(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="Choose an Operation", font=('Segoe UI', '14') )
        label.place(y=32, relx=.5, rely=0, anchor=CENTER)

        cardH = 128
        imageH = 96
        cardS = 16

        COMMANDS = [
            ('Map Project', 'project', 'MapProject', 'Transform a PDS image to a GIS/Map Format', 'Copy a raw PDS image into your local directory.'),
            ('Co-Registration', 'coreg', 'CoRegister', 'Stack Two Map Orbital Images', 'Put your two input Map-Projected images in one local directory.'),
            ('Mosaic', 'mosaic', 'Mosaic', 'Combines Several Map-Projected Orbital Images', 'Put all your input Map-Projected images in one local directory.')
        ]

        self.cards = {}

        hlbg = "#ffffff"
        hlbgA = "#18bc9c"
        hlth = 3
        hlthA = 3 

        for index, (text, val, page, desc, req) in enumerate(COMMANDS):
            card = Frame(self, highlightbackground=hlbg, highlightthickness=hlth)
            card.place(y=132 + (index * cardH) + (index * cardS), relx=.5, relwidth=0.9, height=cardH, anchor=CENTER)

            # Event Functions            
            def enter_card(index):
                return lambda e: self.cards[index].config(highlightbackground=hlbgA, highlightthickness=hlthA)
            def leave_card(index):
                return lambda e: self.cards[index].config(highlightbackground=hlbg, highlightthickness=hlth)
            def select(page):
                return lambda e: parent.show_frame(page)

            img = PhotoImage(file="assets/" + val + ".png")
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
                font=('Segoe UI', '16')
            )
            label.place(y=20, x=128)
            label2 = ttk.Label(
                card, 
                text=desc,
                font=('Segoe UI', '12')
            )
            label2.place(y=50, x=128)
            label3 = ttk.Label(
                card, 
                text=req,
                font=('Segoe UI', '10')
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

    def setPage(page):
        print('splashDRAW', page)