import threading
from tkinter import Frame, Scrollbar, Text, CENTER, SW, NW, DISABLED, END, INSERT
import ttkbootstrap as ttk
from ttkbootstrap.constants import INFO, DANGER

import subprocess

from pomm_ui.components.tophelp import TopHelp


def run():
    Run()


class Run(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.isRunning = False

        # Back
        self.buttonBack = ttk.Button(
            self,
            text="Back",
            command=lambda: self.backward()
        )
        self.buttonBack.place(rely=1.0, relx=0.0, relwidth=0.2, anchor=SW)

        # Run
        self.runButton = ttk.Button(
            self,
            text="RUN",
            bootstyle=(INFO),
            command=lambda: self.run()
        )
        self.runButton.place(rely=1.0, relx=0.2, relwidth=0.8, anchor=SW)

        TopHelp(self, "run")

    def run(self):
        if (self.isRunning is False):
            self.isRunning = True
            state = self.parent.state.get_state()
            planet = state['core']['planet']
            command = state['core']['command']
            params = state[command]
            upf = [
                '# POMM UPF',
                '# AFIDS Planetary Orbital Mapping and Mosaicking User Parameter File',
                '# Generated with POMM UI v' + state['version'],
                '# For command: ' + command.lower(),
                '',
                'planet=' + planet,
                ''
            ]
            for key, value in params.items():
                upf.append(str(key) + '=' + str(value))
            upf = "\n".join(str(x) for x in upf)

            self.upfPrefix = "pommui_" + command.lower()
            self.finalCommand = self.parent.config[command]['command']

            f = open(self.upfPrefix + "_params.upf", "w")
            f.write(upf)
            f.close()

            t = threading.Thread(target=self.execute)
            t.start()
        else:
            self.runButton.configure(
                text="RUN", bootstyle=(INFO))
            self.buttonBack.configure(state="enabled")
            self.isRunning = False

    def execute(self):
        self.runButton.configure(
            text="STOP", bootstyle=(DANGER))
        self.buttonBack.configure(state="disabled")

        process = 'vicarb "' + self.finalCommand + \
            ' ' + self.upfPrefix + '" >& xxlog.log &'
        subprocess.Popen(process,  universal_newlines=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        watchProcess = ['tail', '-f', '--retry', 'xxlog.log']
        wp = subprocess.Popen(watchProcess, universal_newlines=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        self.destroyComponents()

        self.tlabel = ttk.Label(self, text="RUNNING", font=(
            'helvetica', '18', 'bold'), bootstyle=INFO)
        self.tlabel.place(y=32, relx=.5, rely=0, anchor=CENTER)

        self.cmdlabel = ttk.Label(
            self, text=process, font=('helvetica', '12', 'bold'))
        self.cmdlabel.place(y=67, relx=0.5, rely=0, anchor=CENTER)

        self.text = Text(self, height=28, wrap="none",
                         font=('helvetica', '12'),
                         undo=False
                         )

        self.text.place(y=96, relx=0.1, relwidth=0.8, anchor=NW)
        self.displayRunningText(wp)

    def displayRunningText(self, p):
        lines_iterator = iter(p.stdout.readline, b"")
        maxLines = 28
        display = []
        for line in lines_iterator:
            if len(line) > 0 and line != '\r\n':
                display.append(line)
                if len(display) > maxLines:
                    del (display[0])
                self.text.delete('1.0', END)
                for d in display:
                    self.text.insert(INSERT, d)

    def backward(self):
        state = self.parent.state.get_state()
        command = state['core']['command']
        self.parent.show_frame(command)

    def destroyComponents(self):
        try:
            self.tlabel.destroy()
            self.plabel.destroy()
            self.clabel.destroy()
            self.prmlabel.destroy()
            self.v.destroy()
            self.text.destroy()
            self.cmdlabel.destroy()
        except:
            pass

    def onRaise(self):
        state = self.parent.state.get_state()
        planet = state['core']['planet']
        command = state['core']['command']
        params = state[command]

        self.destroyComponents()

        self.tlabel = ttk.Label(self, text="RUN", font=(
            'helvetica', '18', 'bold'), bootstyle=INFO)
        self.tlabel.place(y=32, relx=.5, rely=0, anchor=CENTER)

        self.plabel = ttk.Label(self, text="Planet: " + planet.capitalize(),
                                font=('helvetica', '14'))
        self.plabel.place(y=64, relx=0.1, rely=0)

        self.clabel = ttk.Label(self, text="Operation: " +
                                command.capitalize(), font=('helvetica', '14'))
        self.clabel.place(y=96, relx=0.1, rely=0)

        self.prmlabel = ttk.Label(
            self, text="Parameters:", font=('helvetica', '12'))
        self.prmlabel.place(y=128, relx=0.1, rely=0)

        self.v = Scrollbar(self, orient='vertical')

        self.text = Text(self, height=25, wrap="none",
                         font=('helvetica', '11'),
                         yscrollcommand=self.v.set
                         )

        self.text.place(y=160, relx=0.1, relwidth=0.8, anchor=NW)
        self.v.config(command=self.text.yview)
        self.v.place(in_=self.text, relx=1.0,
                     relheight=1.0, bordermode="outside")

        for key, value in params.items():
            self.text.insert('end', str(key) + '=' + str(value) + '\n')

        self.text.configure(state=DISABLED)
