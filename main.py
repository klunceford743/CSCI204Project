""" Katie Lunceford
This is the main function. It asks for a user input file, converts this
file into a Document object and uses the text in this Document to create
a scatter plot of the top 10 most frequently used words in the document
"""

import Doc as d
import BasicStats as b
import CommandLinePlot as c
import DocumentStreamError as ds

def main():

    file = input('Please enter a file: ' )
    try:
        #converts the file into a document object
        doc = d.Document(file)
    
        words = []
        #makes a new list of all of the words in the file, removing any
        #punctuation and making everything lowercase, so that they will
        #all be counted as the same word
        for sent in doc.getSentences():
            if not sent.string[-1].isalpha():
                s = sent.string[:-1]
            else:
                s = sent.string
            w = [x.lower() for x in s.split()]
            words += w

        #uses the BasicStats object to create a dictionary of the
        #top 10 words used in the document
        stats = b.BasicStats()
        stats.dic = b.BasicStats.createFreqMap(words)
        top = stats.topN(10)

        #makes a list of the number of times each of the top 10 words is used
        num = []
        for key in top:
            num.append(top[key])

        #makes a scatter plot using the number of time the top 10 words are used
        #as the y axis and the rank of those words (most to 10th most, along
        #along the x axis
        num.sort(reverse = True)
        plt = c.CommandLinePlotter()
        plt.twoDScatter(num)

        #makes a list of tuples of the words and their length
        wordList = []
        for key in top:
            wordList.append((key, top[key]))
        wordList.sort(key= lambda tup: tup[1], reverse = True)

        #prints the list of tuples as a key to know which word was the most
        #used to which was the 10th most used
        for i in range(len(wordList)):
            print('Word', i +1, wordList[i][0], end = '; ')

    #handles any exceptions that might occur from the DocumentStream class
    except ds.DocumentStreamError as E:
        print(E.data)
    
main()
