""" Katie Lunceford

This is the BasicStats object that is used to generate stats about given
strings. The only attribute is a dictionary that keeps track of how many
times a word is used.

The methods are topN and bottomN. There is a static method called
createFreqMap
"""

class BasicStats:

    #the initialization function, the only attribute starts off as a blank
    #dictionary
    def __init__(self):
        self.dic = {}

    #can be called before an instance is initialized, takes a list of words
    #as an input and returns a dictionary of what words are used as the keys
    #and the frequency with which they're used as the values
    @staticmethod
    def createFreqMap(wordList):
        wordCount = {}
        for i in range(len(wordList)):
            #checks if the word is already in the dictionary, if it is it
            #adds one to the value, if it is not it adds it to the dictionary
            #with an initial value of 0
            if wordList[i] in wordCount:
                wordCount[wordList[i]] += 1
            else:
                wordCount[wordList[i]] = 1
        return wordCount
    """
    The number of operations in this method is n, where n is the length
    of wordList. The theta notation of this is also n.
    """

    #uses the dictionary stored in self, and inputs a number, then outputs
    #a dictionary of just the top n most frequently used words
    def topN(self, n):
        top = {}
        #creates a list of n 0s
        topNums = [0 for x in range(n)]
        for key in self.dic:
            #if the value in the dic is greater than the smallest number in
            #topNums, then it replaces that value
            if self.dic[key] > topNums[0]:
                topNums[0] = self.dic[key]
            #sorts the top numbers so the smallest value is first
            topNums.sort()

        #iterates through the dictionary and if the value matches one of the
        #top n most frequently used numbers, then it adds that to a new
        #dictionary that only stores the most frequently used words
        for key in self.dic:
            if self.dic[key] in topNums:
                top[key] = self.dic[key]
                
                #if the word is used the least number of times that would
                #qualify it to be in the top list, then the first value of
                #topNums is deleted so we don't end up with more than n words
                if self.dic[key] == topNums[0]:
                    del topNums[0]
        return top
    """
    The number of operations in this method is 2n, where n is the
    length of self.dic. The theta notation of this is just n.
    """

    #a method similar to topN that uses the dictionary stored in self, and
    #inputs a number, then outputs a dictionary of just the bottom n most
    #frequently used words
    def bottomN(self, n):
        bottom = {}
        #creates a list of n 0s
        bottomNums = [0 for x in range(n)]
        for key in self.dic:
            #if the smallest value is 0 that automatically gets replaced
            if bottomNums[0] == 0:
                bottomNums[0] = self.dic[key]
                
            #if there are no zeros then it checks if the value is smaller
            #than the largest number in the list, and if it is then it
            #replaces that number
            elif self.dic[key] < bottomNums[-1]:
                bottomNums[-1] = self.dic[key]
            #bottomNums is sorted each time
            bottomNums.sort()

        #iterates through the dictionary and if the value matches one of the
        #bottom n least frequently used numbers, then it adds that to a new
        #dictionary that only stores the least frequently used words
        for key in self.dic:
            if self.dic[key] in bottomNums:
                bottom[key] = self.dic[key]

                #if the word is used the most number of times that it would
                #qualify for the bottom list, then the last value of bottomNums
                #is deleted so we don't end up with more than n words
                if self.dic[key] == bottomNums[-1]:
                    del bottomNums[-1]            
        return bottom

    """
    Yes, it would be faster to do this at the same time. Because both methods
    are using the same loops, if we put this in one method, then we would only
    have to go through each loop once and create both lists topNums and
    bottomNums at the same time.
    """
