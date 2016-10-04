"""Katie Lunceford and Jon Li
sLink class
"""


class sllist(object):
    def __init__(self, head = None):
        self.head = head

    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        rn = self.head
        c = 0 # c is the count 
        while rn:
            c+=1
            rn = rn.get_next()
        return c 

    def search(self, data):
        rn = self.head
        status = False
        while status is False and rn:
            if rn.get_data() == data:
                status = True
            else:
                rn = rn.get_next()
        if rn is None:
            raise ValueError("Data is invalid")
        return rn

    def delete(self, data):
        prev = None
        rn = self.head
        status = False
        while status and status is False:
            if rn.get_data() == False:
class Node(object):
    def __init__(self,data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.new_next = new_next

    
        
