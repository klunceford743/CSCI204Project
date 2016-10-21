""" Katie Lunceford
"""
import codecs

class TextFilter:

    def __init__(self, doc, stringlist):
        file = open(doc, 'r', encoding = 'utf-8')
        self.doc = file.read()
        self.strings = stringlist

    def normalizeWhite(self):
        if self.doc[0].isspace():
            s = ' '
        else:
            s = self.doc[0]
        for x in range(1, len(self.doc)):
            if self.doc[x].isspace() and not s[-1].isspace():
                s += ' '
            elif not self.doc[x].isspace():
                s+= self.doc[x]
        self.doc = s

    def normalizeCase(self):
        self.doc = self.doc.lower()

    def stripNull(self):
        s = ''
        for char in self.doc:
            if ord(char) < 128:
                s += char
        self.doc = s

    def stripNumbers(self):
        s = ''
        for char in self.doc:
            if not char.isnumeric():
                s += char
        self.doc = s

    def apply(self):
        for filt in self.strings:
            if filt == 'nw':
                self.normalizeWhite()
            elif filt == 'nc':
                self.normalizeCase()
            elif filt == 'sn':
                self.stripNull()
            elif filt == 'snum':
                self.stripNumbers()
            else:
                print('Not a valid filter.')




            
