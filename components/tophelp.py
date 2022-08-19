from tkinter import PhotoImage, Button, NE
from components.help import Help


def TopHelp(self, name):
    headH = 30
    self.helpIcon = PhotoImage(file="assets/help.png")
    buttonHelp = Button(
        self,
        image=self.helpIcon,
        command=lambda: Help(name),
        width=headH,
        height=headH
    )
    buttonHelp.configure(background='#FFFFFF', activebackground='#FFFFFF')
    buttonHelp.place(width=headH, height=headH, relx=1.0, rely=0.0, anchor=NE)

    # Home button
    self.homeIcon = PhotoImage(file="assets/home.png")
    buttonHome = Button(
        self,
        image=self.homeIcon,
        command=lambda: self.parent.show_frame('Splash'),
        width=headH,
        height=headH
    )
    buttonHome.configure(background='#FFFFFF', activebackground='#FFFFFF')
    buttonHome.place(width=headH, height=headH, relx=0.0, rely=0.0)
