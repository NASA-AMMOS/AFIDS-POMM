from tkinter import Frame, Label, W, E, BOTTOM, CENTER, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS, OUTLINE

def planet():
    Planet()

class Planet(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="Choose a Celestial Body", font=('Segoe UI', '14') )
        label.place(y=32, relx=.5, rely=0,anchor=CENTER)

        celestialBody = StringVar()
        celestialBody.set('')

        PLANETS = self.parent.config['planets']

        for (index, planet) in enumerate(PLANETS):
            name = planet['name']
            value = planet['value']
            rb = ttk.Radiobutton(self, text=name, variable=celestialBody, value=value, bootstyle="success")
            rb.place(y=(90 + index * 30), relx=.25, rely=0, anchor=W)

        # Continue
        button = ttk.Button(
            self, 
            text="Continue", 
            command=lambda: parent.show_frame('Command'),
            bootstyle=(SUCCESS, OUTLINE)
        )
        # 30 for headH
        button.pack(side=BOTTOM, padx=12, pady=42, anchor=E)

    def setPage(page):
        print('splashDRAW', page)