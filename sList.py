"""Katie Lunceford and Jon Li
sLink class
"""


class SLink(object):
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def __len__(self):
        runner = self.head
        c = 0 # c is the count 
        while runner is not None:
            c+=1
            runner = runner.next
        return c 

    def remove(self, word):
        prev = None
        runner = self.head
        while runner is not None and runner.data[0] != word:
            prev = runner
            runner = runner.next
        if runner is None:
            return 'The data is not in the list'
        if runner == self.head:
            self.head = runner.next
            del runner
        else:
            prev.next = runner.next
            del runner

    def search(self, word):
        runner = self.head
        state = False
        while runner is not None:
            if runner.data[0] == word:
                state = True
                break
            runner = runner.next
        return state

    def delAll(self):
        runner = self.head
        while runner is not None:
            temp = runner
            runner = runner.next
            del temp
        self.head = None

    def __iter__(self):
        return SLinkIterator(self.head)
                
class Node(object):
    def __init__(self,data = [], next_node = None):
        self.data = data
        self.next = next_node

class SLinkIterator:
    def __init__(self, head):
        self.runner = head
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.runner == None:
            raise StopIteration
        else:
            item = self.runner.data
            self.runner = self.runner.next
            return item

    
        
