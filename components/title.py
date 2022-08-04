from tkinter import Button, NE, messagebox
import ttkbootstrap as ttk

def Title(self, component, startY):
    headH = 30
    
    label = ttk.Label(self, text=component['title'], font=('Segoe UI', '12') )
    label.place(y=startY, relx=0.1)

    buttonHelp = Button(
        self, 
        image=self.helpIcon,
        command=lambda: messagebox.showinfo('POMM Help', component['help']),
        width=headH,
        height=headH
    )
    buttonHelp.configure(background='#FFFFFF', activebackground='#FFFFFF')
    buttonHelp.place(width=20, height=headH, y=startY, relx=0.9, anchor=NE)

    startY = startY + 32

    return startY

        