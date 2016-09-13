"""Katie Lunceford
"""

class DocumentStream:

    def __init__(self, fileName = ''):
        self.fileName = fileName

    def readWhole(self):
        file = open(self.fileName, 'r')
        text = file.read()
        punctuation = ['.', '!', '?', ';']
        sentence = ''
        listSent = []
        i = 0
        while i < len(text):
            sentence += text[i]
            if i < len(text) - 1 and text[i] in punctuation and text[i+1].isspace():
                listSent.append(sentence)
                sentence = ''
                i += 2
            elif i == len(text) - 1:
                listSent.append(sentence)
                break
            else:
                i += 1
        return listSent
                
