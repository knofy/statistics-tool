#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog
import read_csv
import statistics


class Windows:

    def __init__(self, master = None):
        frame = Frame()
        frame.pack()

        self.printButton = Button(frame, text="Create Report", command=self.execute_report)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

        menu = Menu (root)
        root.config(menu=menu)
        submenu = Menu(menu)
        menu.add_cascade(label="Spaltenüberschriften", menu=submenu)
        
        # reads header and content out of chosen file
        header, content = read_csv.read_csv(filename)
        for i in header:
            submenu.add_command(label=i,command=None) #"""Bei Label kommt die erste Spaltenüberschrift hinein, Hier kommt dann die Funktion hinein, die auf die jeweilige Spalte die angeklickt ist verlinkt Hier soll mit einer for Schleife die Subauswahlfelder für die Spalten generiert werden """


    def execute_report(self):
        pass
        # insert statistics-functions here
        # statistics.calc_mean(filename, key)


filename = filedialog.askopenfilename()
root = Tk()

b = Windows(root)
root.mainloop()
