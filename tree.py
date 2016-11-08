""" Katie Lunceford
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None

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
            return Node(val)
        if len(inputAttr) == 1:
            items = []
            for x in range(len(data)):
                items.append(data[x][0])
            val = mostFreq(items)
            return Node(val)





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
    for x in range(len(data[0])):
        items = []
        for y in range(len(data)):
            items.append(data[y][x])
        ent = calculateEntropy(items)

def calculateEntropy(items):
    

