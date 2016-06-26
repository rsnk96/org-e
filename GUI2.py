from tkinter import *
from tkinter.ttk import *

class App(Frame):
        def __init__(self):
                Frame.__init__(self)
    
                self.master.geometry('400x300')
                self.master.title(__file__)
    
                self.pack()

                self.menu = Menu(tearoff=False)
                self.master.config(menu = self.menu)

                fm = self.file_menu = None
                fm = Menu(self.menu, tearoff=False)
                self.menu.add_cascade(label='File', menu = fm)

                fm.add_command(label='Say Hello', command = self.say_hello)
                fm.add_separator()
                fm.add_command(label='Quit', command = self.quit)

                self.mainloop()

        def say_hello(self, *e):
                self.label = Label(self.master, text='Hello there!')
                self.label.pack(anchor=CENTER, fill=NONE, expand=YES, side=LEFT)


App()