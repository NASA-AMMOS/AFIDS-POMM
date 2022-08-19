from tkinter import Toplevel
from tkinterweb import HtmlFrame
import webbrowser


def Help(name):
    with open('assets/help/' + name + '.html', 'r', encoding='utf-8') as f:
        html_string = f.read()

        top = Toplevel()
        top.geometry("1000x700")
        # create the HTML browser
        frame = HtmlFrame(top, messages_enabled=False)
        frame.load_html(html_string)

        def openWebPage(url):
            # Do stuff - insert code here
            webbrowser.open_new_tab(url)  # load the new website

        frame.on_link_click(openWebPage)

        # attach the HtmlFrame widget to the parent window
        frame.pack(fill="both", expand=True)

        top.mainloop()
