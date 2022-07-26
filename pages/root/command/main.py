from tkinter import Frame, Label, W, E, BOTTOM, PhotoImage, Button, CENTER, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS, OUTLINE

def command():
    Command()

class Command(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="Choose an Operation", font=('Segoe UI', '12') )
        label.place(y=30, relx=.5, rely=0, anchor=CENTER)

        labelColor = '#151515'
        labelColorActive = '#02b875'
        cardW = 200
        cardH = 180
        imageH = 50
        cardS = 24

        COMMANDS = [('Map Project', 'project'), ('Co-Registration', 'coreg'), ('Mosaic', 'mosaic')]

        self.cards = {}

        for index, (text, val) in enumerate(COMMANDS):
            card = Frame(self)
            print(1 / len(COMMANDS))
            card.place(y=100, x=(cardW * index + (cardS * (index + 1))), relwidth=(1 / len(COMMANDS)), relheight=0.9)

            img = PhotoImage(file="assets/" + val + ".png")
            button = Button(
                card, 
                image=img,
                command=lambda: parent.show_frame('Planet')
            )
            button.img = img
            button.place(y=0, x=0, width=cardW, height=imageH)

            label = ttk.Button(
                card, 
                text=text, 
                command=lambda: parent.show_frame('Splash'),
                bootstyle=(SUCCESS, OUTLINE)
            )
            label.place(y=180, relx=.5, rely=0, relwidth=0.3, anchor=CENTER)
            self.cards[id] =  button

        # Continue
        button = ttk.Button(
            self, 
            text="Continue", 
            command=lambda: parent.show_frame('Command'),
            bootstyle=(SUCCESS, OUTLINE)
        )
        # 30 for headH
        button.pack(side=BOTTOM, padx=12, pady=42, anchor=E)