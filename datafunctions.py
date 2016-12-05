""" Katie Lunceford
Formatting data
"""
import BasicStats as b
import Doc as d
import SKTree as t
import tree as tr

def dataGenre(documents):
    data = []
    labels = ['author', 'genre']
    for doc in documents:
        data.append([doc.author, assignGenre(doc)])
    return data, labels

def assignGenre(doc):
    if doc.genre == 'short story':
        return 0
    elif doc.genre == 'fiction':
        return 1
    elif doc.genre == 'science fiction':
        return 2
    elif doc.genre == 'horror':
        return 3
    elif doc.genre == 'poem':
        return 4
    else:
        return 5

def dataYear(documents):
    data = []
    labels = ['author', 'year']
    for doc in documents:
        data.append([doc.author, assignYear(doc)])
    return data, labels

def assignYear(doc):
    if int(doc.year) < 1850:
        return 0
    elif int(doc.year) < 1900:
        return 1
    else:
        return 2

def dataTop(documents):
    data = []
    labels = ['author']
    words = []
    for doc in documents:
        doc.generateWhole()
        for sent in doc.getSentences():
            w = [x.lower() for x in sent.string.split()]
            words += w
    stats = b.BasicStats()
    stats.dic = b.BasicStats.createFreqMap(words)
    top = stats.topNHeap(10)
    for x in top:
        labels.append(x[0])
    for doc in documents:
        words = []
        info = [doc.author]
        for sent in doc.getSentences():
            w = [y.lower() for y in sent.string.split()]
            words += w
        for x in labels[1:]:
            if x in words:
                info.append(1)
            else:
                info.append(0)
        data.append(info)
    return data, labels

def dataBottom(documents):
    data = []
    labels = ['author']
    words = []
    for doc in documents:
        doc.generateWhole()
        for sent in doc.getSentences():
            w = [x.lower() for x in sent.string.split()]
            words += w
    stats = b.BasicStats()
    stats.dic = b.BasicStats.createFreqMap(words)
    bottom = stats.bottomNHeap(10)
    for x in bottom:
        labels.append(x[0])
    for doc in documents:
        words = []
        info = [doc.author]
        for sent in doc.getSentences():
            w = [y.lower() for y in sent.string.split()]
            words += w
        for x in labels[1:]:
            if x in words:
                info.append(1)
            else:
                info.append(0)
        data.append(info)
    return data, labels
    
def predData(doc, labels):
    data = [[None]]
    doc.generateWhole()
    words = []
    for sent in doc.getSentences():
        w = [x.lower() for x in sent.string.split()]
        words += w
    for i in range(len(words)):
        if not words[i][-1].isalpha():
            words[i] = words[i][:-1]
    for x in labels[1:]:
        if x in words:
            data[0].append(1)
        else:
            data[0].append(0)

    return data

def trainGenre(documents):
    data, labels = dataGenre(documents)
    s = t.SKTree()
    s.train(data, labels, 10)
    return s

def trainYear(documents):
    data, labels = dataYear(documents)
    s = t.SKTree()
    s.train(data, labels, 10)
    return s

def trainTop(documents):
    data, labels = dataTop(documents)
    s = t.SKTree()
    s.train(data,labels,30)
    return s

def trainBottom(documents):
    data, labels = dataBottom(documents)
    s = t.SKTree()
    s.train(data, labels, 30)
    return s

def trainGenreID(documents):
    data, labels = dataGenre(documents)
    s = tr.DecisionTree()
    s.train(data, labels, 10)
    return s

def trainYearID(documents):
    data, labels = dataYear(documents)
    s = tr.DecisionTree()
    s.train(data, labels, 10)
    return s

def trainTopID(documents):
    data, labels = dataTop(documents)
    s = tr.DecisionTree()
    s.train(data, labels, 30)
    return s

def trainBottomID(documents):
    data, labels = dataBottom(documents)
    s = tr.DecisionTree()
    s.train(data, labels, 30)
    return s

def dataPCA(documents):
    data = []
    labels = ['author']
    words = []
    for doc in documents:
        data.append([doc.author])
        doc.generateWhole()
        for sent in doc.getSentences():
            w = [x.lower() for x in sent.string.split()]
            words += w
    stats = b.BasicStats()
    stats.dic = b.BasicStats.createFreqMap(words)
    top = stats.topNHeap(50)
    for x in top:
        labels.append(x[0])
    for i in range(len(documents)):
        wCount = documents[i].getWordCnt()
        words = []
        for sent in documents[i].getSentences():
            w = [y.lower() for y in sent.string.split()]
            words += w
        for l in labels[1:]:
            cnt = 0
            for w in words:
                if w == l:
                    cnt += 1
            ratio = cnt/wCount
            data[i].append(ratio)
    return data, labels

def predPCA(doc, labels):
    data = [[None]]
    doc.generateWhole()
    wCount = doc.getWordCnt()
    words = []
    for sent in doc.getSentences():
        w = [y.lower() for y in sent.string.split()]
        words += w
    for l in labels[1:]:
        cnt = 0
        for w in words:
            if w == l:
                cnt += 1
        ratio = cnt/wCount
        data[0].append(ratio)
    return data


