from tkinter import Frame, Scrollbar, Text, CENTER, SW, NW, SE, DISABLED
import ttkbootstrap as ttk
from ttkbootstrap.constants import INFO, OUTLINE

from components.tophelp import TopHelp


def run():
    Run()


class Run(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="RUN", font=(
            'Segoe UI', '18'), bootstyle=INFO)
        label.place(y=46, relx=.5, rely=0, anchor=CENTER)

        # Back
        buttonBack = ttk.Button(
            self,
            text="Back",
            command=lambda: self.backward()
        )
        buttonBack.place(rely=1.0, relx=0.0, relwidth=0.2, anchor=SW)

        # Run
        self.runButton = ttk.Button(
            self,
            text="RUN",
            bootstyle=(INFO)
        )
        self.runButton.place(rely=1.0, relx=0.2, relwidth=0.8, anchor=SW)

        TopHelp(self, "run")

    def backward(self):
        state = self.parent.state.get_state()
        command = state['core']['command']
        self.parent.show_frame(command)

    def onRaise(self):
        state = self.parent.state.get_state()
        planet = state['core']['planet']
        command = state['core']['command']
        params = state[command]

        try:
            self.plabel.destroy()
            self.clabel.destroy()
            self.prmlabel.destroy()
            self.v.destroy()
            self.text.destroy()
        except:
            pass

        self.plabel = ttk.Label(self, text="Planet: " + planet.capitalize(),
                                font=('Segoe UI', '14'))
        self.plabel.place(y=64, relx=0.1, rely=0)

        self.clabel = ttk.Label(self, text="Operation: " +
                                command.capitalize(), font=('Segoe UI', '14'))
        self.clabel.place(y=96, relx=0.1, rely=0)

        self.prmlabel = ttk.Label(
            self, text="Parameters:", font=('Segoe UI', '12'))
        self.prmlabel.place(y=128, relx=0.1, rely=0)

        self.v = Scrollbar(self, orient='vertical')

        self.text = Text(self, height=22, wrap="none",
                         font=('Segoe UI', '11'),
                         yscrollcommand=self.v.set
                         )

        self.text.place(y=160, relx=0.1, relwidth=0.8, anchor=NW)
        self.v.config(command=self.text.yview)
        self.v.place(in_=self.text, relx=1.0,
                     relheight=1.0, bordermode="outside")

        for key, value in params.items():
            self.text.insert('end', str(key) + '=' + str(value) + '\n')

        self.text.configure(state=DISABLED)
