"""Katie Lunceford

This is the Document object. It will be constructed as an Abstract Data
Type. It relies on the DocumentStream object. It has a class attribute of
count, and it's individual attributes are: fileName (the name of the file to
be analyzed), refNum (a reference number for the document), sentences (a list
of individual sentences in the document), wordCnt (a count of the words in
the document), charCnt (a count of the characters in the document), and
lineCnt (the number of lines in the document).

The methods in this object are generateWhole, getSentences, setSentences,
getRefNum, getWordCnt, getLineCnt, getCharCnt, setWordCnt, setLineCnt, and setCharCnt
"""

import DocStream as d
import DocumentStreamError as ds

class Document:

    #count increases every time a document is created to give each
    #document its own reference id
    count = 0

    #the initialization of a document takes in a fileName
    #all of the attributes are private besides the fileName
    def __init__(self, fileName):
        self.fileName = fileName
        Document.count += 1
        self.__refNum = Document.count
        self.__sentences = self.generateWhole()
        self.__wordCnt = 0
        self.__charCnt = 0
        self.__lineCnt = 0

    #generates a list of sentences from the document, using the
    #readWhole method from the DocumentStream object, this method
    #is then used in the initialization to set the variable
    #self.__sentences
    def generateWhole(self):
        return d.DocumentStream(self.fileName).readWhole()
    
    #getter for __sentences
    def getSentences(self):
        return self.__sentences
    #setter for __sentences
    def setSentences(self, sentences):
        self.__sentences = sentences
    #getter for __refNum
    def getRefNum(self):
        return self.__refNum
    #setter for __refNum
    def setRefNum(self, refNum):
        self.__refNum = refNum

    #getter for __wordCnt, but not a typical getter, starts by checking
    #if the wordCnt is 0, if it is not then it wordCnt has already been
    #set so it just returns the already set wordCnt, if it is 0, then
    #it uses a loop to sum the wordCount from each sentence in
    #self.__sentences, and sets .__wordCnt and returns wordCnt
    def getWordCnt(self):
        wordCnt = self.__wordCnt
        if wordCnt == 0:
            for i in self.__sentences:
                wordCnt += i.wordCount
            self.setWordCnt(wordCnt)
        return wordCnt

    #getter for __lineCnt, but not a typical getter, starts by checking if
    #the lineCnt is 0, if it is not then lineCnt has already been set so it
    #just returns the already set lineCnt, if it is 0, then it uses a loop
    #to sum the number of '\n' characters from each sentence in
    #self.__sentences and sets.__lineCnt and returns lineCnt
    def getLineCnt(self):
        lineCnt = self.__lineCnt
        if lineCnt == 0:
            for i in self.__sentences:
                for char in i.string:
                    if char == '\n':
                        lineCnt += 1
            self.setLineCnt(lineCnt)
        return lineCnt
    #getter for __charCnt, but not a typical getter, starts by checking if
    #the charCnt is 0, if it is not then lineCnt has already been set so it
    #just returns the already set charCnt, if it is 0, then it uses a loop
    #to sum the charCnt from each sentence in self.__sentences and sets
    #.__charCnt and returns charCnt
    def getCharCnt(self):
        charCnt = self.__charCnt
        if charCnt == 0:
            for i in self.__sentences:
                charCnt += i.charCount
            self.setCharCnt(charCnt)
        return charCnt
    #setter for wordCnt
    def setWordCnt(self, wordCnt):
        self.__wordCnt = wordCnt
    #setter for getCnt
    def setLineCnt(self, lineCnt):
        self.__lineCnt = lineCnt
    #setter for charCnt
    def setCharCnt(self, charCnt):
        self.__charCnt = charCnt

            

