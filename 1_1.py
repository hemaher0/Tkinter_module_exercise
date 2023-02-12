import tkinter as tk                                                            #This line imports the Tkinter module into your program's namespace, but renames it as tk.


class Application(tk.Frame):                                                    #Your application class must inherit from Tkinter's Frame class
    def __int__(self, master=None):
        tk.Frame.__init__(self, master)                                         #Calls the constructor for the parent class, Frame
        self.grid()                                                             #Necessary to make the application actually appear on the screen
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)       #Creates a button labeled "Quit"
        self.quitButton.grid()                                                  #Places the button on the application


app = Application()                                                             #The main program stats here by instantiating the Application class.
app.master.title('Sample application')                                          #This method call sets the title of the window to "Sample application"
app.mainloop()                                                                  #Starts the application's main loop, waiting for mouse and keybourdd events.
