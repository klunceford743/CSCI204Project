""" Katie Lunceford

Summary:
The article was a brief introduction to GUI (graphical user interface)
programming, using the Python module tkinter. Event driven programming is
when our program is able to respond to actions that the user makes, such
as clicking on the mouse or pressing a button. Widgets are the GUI elements that
allow us to build our interface. The article uses a few examples of
different GUI classes that respond to user actions, such as clicking on a
button. It then goes on to talk about the different ways to design the
interface layout, including the pack method and the grid method. Finally,
it describes how we can costumize the events by having them respond to a
a specific button or mouse click, etc. 
"""


from tkinter import Tk, Label, Button, Entry, StringVar, END, W, E
from plotting import *
import Doc as d
import BasicStats as b
import CommandLinePlot as c
import DocumentStreamError as ds

class UserGUI:

    def __init__(self, master):
        self.master = master
        master.title("Graphing")

        self.file = ''
        self.entered_file = ''

        self.file_label_text = StringVar()
        self.file_label_text.set(self.file)
        self.file_label = Label(master, textvariable=self.file_label_text)

        self.label = Label(master, text="File:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.bar_button = Button(master, text="Bar Graph", command=lambda: self.update("bar"))
        self.scatter_button = Button(master, text="Scatter Plot", command=lambda: self.update("scatter"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.file_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.bar_button.grid(row=2, column=0)
        self.scatter_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_file = ''
            return True

        try:
            self.entered_file = str(new_text)
            return True
        except:
            return True

    def update(self, method):
        if method == 'reset':
            self.file = ''
            num = []
            self.file_label_text.set(self.file)
            self.entry.delete(0, END)
            return
        try:
            doc = d.Document(self.entered_file)
            doc.generateWhole()
            words = []

            for sent in doc.getSentences():
                if not sent.string[-1].isalpha():
                    s = sent.string[:-1]
                else:
                    s = sent.string
                w = [x.lower() for x in s.split()]
                words += w
            stats = b.BasicStats()
            stats.dic = b.BasicStats.createFreqMap(words)
            top = stats.topN(10)

            num = []
            for key in top:
                num.append(top[key])
            num.sort(reverse = True)
                
            if method == "bar":
                plot = Plotter(num)
                plot.barGraph()
                self.file = self.entered_file
            elif method == "scatter":
                plot = Plotter(num)
                plot.scatterPlot()
                self.file = self.entered_file
        except ds.DocumentStreamError as E:
            print(E.data)


        self.file_label_text.set(self.file)
        self.entry.delete(0, END)

root = Tk()
my_gui = UserGUI(root)
root.mainloop()
