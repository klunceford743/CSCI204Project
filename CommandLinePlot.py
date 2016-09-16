"""Katie Lunceford

The CommandLinePlotter object that will be used to generate scatter plots. The only
attribute is the plot which holds a twoD array that will show axis and the points on the
scatter plot.

It's methods are generatePlane and twoDScatter
"""

class CommandLinePlotter:
    
    #the initialization method starts off with a blank plot.
    def __init__(self):
        self.plot = []

    #a method that generates a blank plot (labeled y and x axes) given a range for x and y
    def generatePlane(self, xStart, xEnd, yStart, yEnd):
        self.plot = []
        y = yEnd
        #creates a list of three spaces for each x value
        lines = ['   ' for i in range(xEnd-xStart+2)]
        
        while y >= yStart:
            #creates a string of the y value, and the appropriate number of spaces and a |
            #to generate the y axis
            axis = str(y) + ' '*(3-len(str(y))) + '|'
            
            #adds the list of blank spaces so the dimensions of the plot will be
            #consistent and appends this to the plot
            self.plot.append([axis]+lines)
            y-=1

        #creates the x axis using the appropriate number of underscores to generate
        #the line based off of how many x coordinates there are
        underScore = ['___' for i in range(xEnd - xStart + 2)]

        #creates a blank spt before the x axis begins and appends it to the plot
        secLast = [ '   |'] + underScore
        self.plot.append(secLast)

        #generates the x axis using the x values and appends it to the plot
        xAxis = [str(x) + ' '*(3-len(str(x))) for x in range(xStart, xEnd + 1)]
        lastLine = ['    '] + xAxis
        self.plot.append(lastLine)

    #a method that creates a scatter plot given two lists (the second list is optional)
    #if the second list is left blank, the first list creates the y coordinates and
    #the x coordinates are 1 to the length of the first list
    #if there are two lists given, the first list is the x coordinates and the
    #second list is the y coordinates
    def twoDScatter(self, list1, list2 = []):

        #if list2 is blank, it sets y as list1 and x as 1 to the length of list1
        if list2 == []:
            y = list1
            x = [i for i in range(1,len(list1) + 1)]
 
        else:
            x = list1
            y = list2

        #gets the range for the x and y axes
        yEnd = max(y)
        yStart = min(y)
        xEnd = max(x)
        xStart = min(x)

        #uses generatePlane to create a blank plot
        self.generatePlane(xStart, xEnd, yStart, yEnd)

        #for each x value, it plots a mark according to the given x and y coordinates
        for i in range(len(x)):
                self.plot[yEnd - y[i]][x[i]-xStart + 1] = 'x  '

        #loop to print the plot as a string
        for line in self.plot:
            string = ''
            for item in line:
                string += str(item)
            print(string)
