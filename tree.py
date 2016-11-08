""" Katie Lunceford
"""

import math

class Node:

    def __init__(self, data, values):
        self.data = data
        self.count = 0
        self.values = values
        self.children = [None]*len(values)

class DecisionTree:

    def __init__(self):
        self.root = None

    def train(self, data, inputAttr, maxDepth):
        if list1 == []:
            raise Exception
        state = True
        val = data[0][0]
        for x in range(len(data)):
            if data[x][0] != val:
                state = False
                break
        if state:
            return Node(val, 0)
        if len(inputAttr) == 1:
            items = []
            for x in range(len(data)):
                items.append(data[x][0])
            val = mostFreq(items)
            return Node(val, 0)
        ind = maxGain(data)
        keys = []
        for x in data:
            if not (data[x][ind] in keys):
                keys.append(data[x][ind])
        newNode = Node(inputAttr[ind],keys)
        for x in range(len(keys)):
            newData = []
            for y in data:
                if y[ind] == keys[x]:
                    newData.append(y)
            newInput = inputAttr[:ind] + inputAttr[ind:]
            newNode.children[x] = train(newData, inputAttr, maxDepth)
        
            





def mostFreq(items):
    dic = {}
    for i in range(len(items)):
        if items[i] in dic:
            dic[items[i]] += 1
        else:
            dic[items[i]] = 1
    maximum = max(dic, key=dic.get)
    return maximum

def maxGain(data):
    entropy = 1
    loc = 0
    for x in range(1,len(data[0])):
        items = []
        for y in range(len(data)):
            items.append([data[y][0],data[y][x]])
        ent = calculateEntropy(partition(items))
        if ent < entropy:
            entropy = ent
            loc = x
    return loc

def partition(twoDList):
    parts = []
    keys = []
    
    for x in range(len(twoDList)):
        if not (twoDList[x][1] in keys):
            keys.append(twoDList[x][1])
            
    for y in keys:
        l = []
        for x in range(len(twoDList)):
            if twoDList[x][1] == y:
                l.append(twoDList[x][0])
        parts.append(l)
    return parts

def calculateEntropy(partList):
    totEnt = 0
    totLen = 0
    for x in partList:
        totLen += len(x)
    for x in partList:
        ent = 0
        keys = []
        for y in x:
            if not (y in keys):
                keys.append(y)
        for key in keys:
            count = 0
            for y in x:
                if y == key:
                    count += 1
            length = len(x)
            val = -(count/length)* math.log(count/length,2)
            ent += val
        totEnt += (len(x)/totLen)*ent
    return totEnt

def generateTests():
    l = [['no','small','no','average','good'], \
         ['no','small','no','light','average'],\
         ['yes','small','yes','average','bad'],\
         ['yes','medium','no','heavy','bad'], \
         ['yes','large','no','average','bad'],\
         ['no','medium','no','light','bad'],\
         ['no','large','yes','heavy','bad'],\
         ['no','large','no','heavy','bad'], \
         ['yes','medium','yes','light','bad'],\
         ['yes','large','no','average','bad'],\
         ['no','small','no','light','good'],\
         ['no','small','no','average','average'],\
         ['no','medium','no','heavy','bad'],\
         ['no','small','yes','average','average'],\
         ['no','medium','no','heavy','bad']]
    return l
