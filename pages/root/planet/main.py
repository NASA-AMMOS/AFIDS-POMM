from tkinter import Frame, Label, W, E, BOTTOM, CENTER, StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS, OUTLINE, DISABLED

def planet():
    Planet()

class Planet(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        label = ttk.Label(self, text="Choose a Celestial Body", font=('Segoe UI', '14') )
        label.place(y=32, relx=.5, rely=0, anchor=CENTER)
        
        self.continueButton = ttk.Button(
            self, 
            text="Continue", 
            command=lambda: self.next(),
            bootstyle=(OUTLINE, DISABLED),
            state="disabled"
        )
        # 30 for headH
        self.continueButton.pack(side=BOTTOM, padx=12, pady=42, ipadx=42, anchor=E)

        self.celestialBody = StringVar()
        self.celestialBody.trace('w', self.validate)
        self.celestialBody.set('')

        PLANETS = self.parent.config['planets']

        for (index, planet) in enumerate(PLANETS):
            name = planet['name']
            value = planet['value']
            rb = ttk.Radiobutton(self, text=name, variable=self.celestialBody, value=value, bootstyle="success")
            rb.place(y=(90 + index * 30), relx=.25, rely=0, anchor=W)

        # Continue


    def setPage(page):
        print('splashDRAW', page)
        
    def validate(self, a, b, c):
        print(a,b,c, self.celestialBody.get())
        if(self.celestialBody.get()):
            self.continueButton.configure(bootstyle=(SUCCESS), state="enabled")
            return True
        return False

    def next(self):
        if(self.validate(None, None, None)):
            self.parent.show_frame('Command')

