from tkinter import Frame, Label, W, E, SW, BOTTOM, CENTER, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import INFO, OUTLINE, DISABLED
from components.tophelp import TopHelp


def planet():
    Planet()


class Planet(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="Choose a Planet/Moon",
                          font=('Segoe UI', '16', 'bold'))
        label.place(y=32, relx=.5, rely=0, anchor=CENTER)

        self.continueButton = ttk.Button(
            self,
            text="Continue",
            command=lambda: self.next(),
            bootstyle=(OUTLINE, DISABLED),
            state="disabled"
        )
        self.continueButton.place(relx=0.0, rely=1.0, relwidth=1.0, anchor=SW)

        self.celestialBody = StringVar()
        self.celestialBody.trace('w', self.validate)
        self.celestialBody.set('')

        PLANETS = self.parent.config['planets']

        for (index, planet) in enumerate(PLANETS):
            name = planet['name']
            value = planet['value']
            rb = ttk.Radiobutton(
                self, text=name, variable=self.celestialBody, value=value, bootstyle=("outline-toolbutton", INFO))
            rb.place(y=(86 + index * 44), relx=0.5, rely=0, anchor=CENTER)

        TopHelp(self, "planet")

    def validate(self, a, b, c):
        if (self.celestialBody.get()):
            self.continueButton.configure(bootstyle=(INFO), state="enabled")
            return True
        return False

    def next(self):
        if (self.validate(None, None, None)):
            self.parent.state.set_state(
                'core', 'planet', self.celestialBody.get())
            self.parent.show_frame('Command')
