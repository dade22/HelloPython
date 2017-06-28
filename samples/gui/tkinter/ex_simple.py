""" GUI: only a button """

#!/usr/bin/env python3
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()

"""
line 1: Hashbang directive to the program launcher, allowing the selection of an appropriate interpreter executable, when self-executing.[8]
line 2: This line imports the Tkinter module into your program's namespace, but renames it as tk.
line 4: Your application class must inherit from Tkinter's Frame class.
line 6: Calls the constructor for the parent class, Frame.
line 7: Necessary to make the application actually appear on the screen.
line 11: Creates a button labeled “Quit”.
line 12: Places the button on the application.
line 14: The main program starts here by instantiating the Application class.
line 15: This method call sets the title of the window to “Sample application”.
line 16: Starts the application's main loop, waiting for mouse and keyboard events.
"""
