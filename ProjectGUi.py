import sys
from tkinter import *

def bs():
    pass

docEnt = StringVar()

Gui1 = Tk()
Gui1.geometry('1000x500')
Gui1.title("CSCI 204 Final Project")

authorLabel = Label(Gui1,text='Jonathan Li and Katie Lunceford',fg='white',bg='black')
authorLabel.pack()

DescriptionLabel = Label(Gui1,text='This program implements machine learning techniques for the purpose of authorship attribution',fg='white',bg='black')
DescriptionLabel.pack()

AddDocumentButton = Button(Gui1,text='Add Document',command=bs)
AddDocumentButton.pack()

RemoveDocumentButton = Button(Gui1,text='Remove Document',command=bs)
RemoveDocumentButton.pack()

docEntry = Entry(Gui1, textvariable = docEnt).pack()
