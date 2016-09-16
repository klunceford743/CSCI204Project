"""Katie Lunceford
This is the DocumentStream object. The only attribute is the fileName that
it uses to read the text from a file.

The methods are readWhole and writeWhole.
"""
import Sentence as s
import DocumentStreamError as d

class DocumentStream:

    #the initialization function, takes fileName as an optional input, if
    #file name is left blank then it just holds an empty string
    def __init__(self, fileName = ''):
        self.fileName = fileName

    #a method that will return a list of all of the sentences in the file
    def readWhole(self):
        try:
            #raises a DocumentStreamError if the file does not exist or it
            #can't find it
            file = open(self.fileName, 'r')
        except:
            raise d.DocumentStreamError('File not found')

        #reads the whole file and stores it in text
        text = file.read()
        punctuation = ['.', '!', '?', ';']
        string = ''
        listSent = []
        i = 0

        #loops through the text and adds each character to a string,
        #if the character is in the punctuation list, or the next two
        #characters are breaks, then it adds the string to the list of
        #sentences and sets the string back to empty
        while i < len(text):
            string += text[i]
            if text[i] in punctuation:
                listSent.append(s.Sentence(string))
                string = ''
            elif i > 1 and text[i] == '\n' and text[i-1] == '\n':
                listSent.append(s.Sentence(string))
                string = ''
            #adds the last sentence to the list
            elif i == len(text) - 1:
                listSent.append(s.Sentence(string))
                break
            i += 1
            
        return listSent

    #a method that prints out the text with one sentence per line
    def writeWhole(self):
        
        listSent = self.readWhole()
        for i in listSent:
            #a statement that keeps track of whether or not the sentence is
            #blank, if it is then it won't be printed
            sentBlank = True
            for char in range(len(i.string)):
                if not i.string[char].isspace():
                    #if the character is not a space then the sentence isn't
                    #blank
                    sentBlank = False
                elif i.string[char] == '\n':
                    #if the character is a line break then it changes it to
                    #a space
                    i.string = i.string[:char] + ' ' + i.string[char + 1:]
            #prints the sentence if it is not blank
            if not sentBlank:
                print(i.string)
